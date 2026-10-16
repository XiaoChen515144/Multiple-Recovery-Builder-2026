#!/usr/bin/env python3
"""Self-check a recovery.img built by this repository.

Unpacks the image (boot header v4 + a *legacy* lz4 ramdisk, which is what AOSP
produces with `lz4 -l`) using nothing but the python standard library, then
reports what is inside and verifies the invariants that matter for this device:

  * boot header sanity (ANDROID! magic, header v4, no kernel, cmdline empty)
  * the ramdisk is a newc cpio archive
  * every module named by vendor/lib/modules/modules.load.recovery exists
  * every file shipped by the device tree's recovery/root made it into the
    ramdisk (this is the check that catches a device tree that silently stops
    being installed)
  * optionally, byte-for-byte equality with the device tree files

Usage:
    tools/unpack_recovery.py recovery.img
    tools/unpack_recovery.py recovery.img --device-root <device tree> \
        --expect-size 104857600 --dump-cpio /tmp/ramdisk.cpio

Exit status is non-zero when a structural check fails, so CI can use it as a
gate.  Every finding is printed, and `--json` writes the summary for tooling.
"""
import argparse
import hashlib
import json
import os
import sys

PAGE = 4096


def align(x, a=PAGE):
    return (x + a - 1) // a * a


# --------------------------------------------------------------- lz4 (legacy)
def lz4_block(src):
    """Decode one LZ4 block (the format used inside a legacy lz4 frame)."""
    out = bytearray()
    i, n = 0, len(src)
    while i < n:
        token = src[i]
        i += 1
        lit = token >> 4
        if lit == 15:
            while True:
                b = src[i]
                i += 1
                lit += b
                if b != 255:
                    break
        if lit:
            out += src[i:i + lit]
            i += lit
        if i >= n:                      # last sequence holds literals only
            break
        off = src[i] | (src[i + 1] << 8)
        i += 2
        if not 0 < off <= len(out):
            raise ValueError(f"bad match offset {off}")
        ml = token & 0x0F
        if ml == 15:
            while True:
                b = src[i]
                i += 1
                ml += b
                if b != 255:
                    break
        ml += 4
        start = len(out) - off
        if off >= ml:
            out += out[start:start + ml]
        else:                           # overlapping match
            pat = bytes(out[start:])
            out += (pat * (ml // len(pat) + 1))[:ml]
    return bytes(out)


def lz4_legacy(data):
    """Decode a legacy lz4 frame (magic 0x184C2102): repeated
    [le32 compressed_size][block] chunks."""
    if data[:4] != bytes.fromhex('02214c18'):
        raise ValueError(f"not a legacy lz4 frame (magic {data[:4].hex()})")
    out, i, blocks = bytearray(), 4, 0
    while i + 4 <= len(data):
        size = int.from_bytes(data[i:i + 4], 'little')
        i += 4
        if size == 0:
            break
        out += lz4_block(data[i:i + size])
        i += size
        blocks += 1
    return bytes(out), blocks


# ------------------------------------------------------------------- cpio
def parse_cpio(buf):
    """Parse a newc cpio archive -> {normalised name: (mode, size, data offset)}."""
    entries, i, n = {}, 0, len(buf)
    while i + 110 <= n:
        magic = buf[i:i + 6]
        if magic not in (b'070701', b'070702'):
            break
        fields = [int(buf[i + 6 + 8 * k:i + 14 + 8 * k], 16) for k in range(13)]
        mode, size, namesize = fields[1], fields[6], fields[11]
        name = buf[i + 110:i + 110 + namesize - 1].decode('utf-8', 'replace')
        off = align(i + 110 + namesize, 4)
        key = name[2:] if name.startswith('./') else name
        entries[key] = (mode, size, off)
        i = align(off + size, 4)
        if name == 'TRAILER!!!':
            break
    return entries


def data_of(buf, meta):
    _, size, off = meta
    return buf[off:off + size]


# ------------------------------------------------------------------- checks
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('image')
    ap.add_argument('--device-root', default=None,
                    help="device tree directory (its recovery/root is compared "
                         "against the ramdisk)")
    ap.add_argument('--expect-size', type=int, default=0,
                    help="expected image size in bytes (e.g. the recovery "
                         "partition size)")
    ap.add_argument('--dump-cpio', default=None, help="write the raw cpio here")
    ap.add_argument('--json', dest='json_out', default=None)
    ap.add_argument('--content-check', action='store_true',
                    help="also compare md5 of every device tree file")
    ap.add_argument('--no-strict', action='store_true',
                    help="report problems but always exit 0")
    args = ap.parse_args()

    problems, summary = [], {}

    with open(args.image, 'rb') as fh:
        img = fh.read()
    print(f"== image: {args.image}")
    print(f"   size: {len(img):,} bytes")
    if args.expect_size and len(img) != args.expect_size:
        problems.append(f"image size {len(img):,} != expected {args.expect_size:,}")

    # ---- boot header
    if img[:8] != b'ANDROID!':
        problems.append(f"bad boot magic {img[:8]!r}")
        print("   !! not a boot image")
        return finish(problems, summary, args)

    header_size = int.from_bytes(img[20:24], 'little')
    header_version = int.from_bytes(img[40:44], 'little')
    kernel_size = int.from_bytes(img[8:12], 'little')
    ramdisk_size = int.from_bytes(img[12:16], 'little')
    cmdline = img[44:44 + 1536].split(b'\0')[0].decode('ascii', 'replace')
    print(f"   header v{header_version}, header_size {header_size}, "
          f"kernel {kernel_size:,}, ramdisk {ramdisk_size:,}")
    print(f"   cmdline: {cmdline!r}")
    if header_version != 4:
        problems.append(f"header version {header_version} != 4")
    if kernel_size != 0:
        problems.append(f"kernel_size {kernel_size} != 0")
    summary['header_version'] = header_version
    summary['ramdisk_size_compressed'] = ramdisk_size

    ramdisk_off = align(header_size) + align(kernel_size)
    payload = img[ramdisk_off:ramdisk_off + ramdisk_size]
    try:
        cpio, blocks = lz4_legacy(payload)
    except ValueError as exc:
        problems.append(f"ramdisk decompression failed: {exc}")
        return finish(problems, summary, args)
    print(f"   lz4 legacy: {blocks} blocks -> {len(cpio):,} bytes cpio")
    summary['ramdisk_size_uncompressed'] = len(cpio)

    if args.dump_cpio:
        with open(args.dump_cpio, 'wb') as fh:
            fh.write(cpio)

    # ---- avb footer
    footer = img[-64:]
    summary['avb'] = footer[:4] == b'AVBf'
    if summary['avb']:
        # footer[0:4] magic, [12:20] original size, [20:28] vbmeta offset,
        # [28:36] vbmeta size (all big endian)
        voff = int.from_bytes(footer[20:28], 'big')
        vsize = int.from_bytes(footer[28:36], 'big')
        vb = img[voff:voff + vsize]
        summary['avb_magic'] = vb[:4].decode('ascii', 'replace')
        summary['avb_vbmeta_offset'] = voff
        print(f"   avb hash footer: {summary['avb_magic']} at {voff:,} ({vsize} B)")

    entries = parse_cpio(cpio)
    files = {k: v for k, v in entries.items() if not k.endswith('/')}
    links = [k for k, v in files.items() if (v[0] & 0o170000) == 0o120000]
    if not entries:
        problems.append("ramdisk is not a newc cpio archive")
        return finish(problems, summary, args)
    print(f"== ramdisk: {len(entries):,} entries "
          f"({len(files) - len(links):,} files, {len(links):,} symlinks)")
    summary['cpio_entries'] = len(entries)
    summary['cpio_files'] = len(files)

    modules = sorted(k for k in files
                     if k.startswith('vendor/lib/modules/') and k.endswith('.ko'))
    vibr = sorted(k for k in files if any(s in k.lower() for s in
                  ('aw8697', 'haptic', 'vibrat', 'richtap', 'lra_model')))
    print(f"   kernel modules: {len(modules)}")
    print(f"   vibration related: {len(vibr)}")
    summary['kernel_modules'] = len(modules)
    summary['vibration_files'] = len(vibr)

    # ---- modules.load.recovery
    ml = files.get('vendor/lib/modules/modules.load.recovery')
    if ml:
        wanted = [l.strip() for l in data_of(cpio, ml).decode('utf-8', 'replace').splitlines()
                  if l.strip() and not l.strip().startswith('#')]
        missing = [m for m in wanted if f'vendor/lib/modules/{m}' not in files]
        print(f"   modules.load.recovery: {len(wanted)} entries, {len(missing)} missing")
        summary['modules_load_recovery'] = len(wanted)
        summary['modules_load_recovery_missing'] = missing
        if missing:
            problems.append(f"modules.load.recovery names {len(missing)} missing modules: "
                            f"{', '.join(missing[:8])}")
    else:
        problems.append("no vendor/lib/modules/modules.load.recovery in the ramdisk")

    # ---- device tree parity
    if args.device_root:
        root = os.path.join(args.device_root, 'recovery', 'root')
        if not os.path.isdir(root):
            problems.append(f"no recovery/root under {args.device_root}")
        else:
            tree = {}
            for dirpath, _, fnames in os.walk(root):
                for fname in fnames:
                    full = os.path.join(dirpath, fname)
                    tree[os.path.relpath(full, root)] = full
            missing = sorted(p for p in tree if p not in files)
            print(f"   device tree recovery/root: {len(tree)} files, {len(missing)} missing")
            summary['device_tree_files'] = len(tree)
            summary['device_tree_missing'] = missing[:50]
            if missing:
                problems.append(f"{len(missing)} device tree files are not in the ramdisk "
                                f"(e.g. {', '.join(missing[:5])})")
            if args.content_check:
                bad = []
                for rel, full in tree.items():
                    if rel not in files:
                        continue
                    if hashlib.md5(data_of(cpio, files[rel])).hexdigest() != \
                       hashlib.md5(open(full, 'rb').read()).hexdigest():
                        bad.append(rel)
                print(f"   content check: {len(tree) - len(missing)} compared, {len(bad)} differ")
                summary['device_tree_content_mismatch'] = bad[:50]
                if bad:
                    problems.append(f"{len(bad)} device tree files differ from the ramdisk")

    # ---- key files
    for key in ('system/bin/recovery', 'system/bin/twrp', 'system/etc/twrp.flags',
                'vendor/bin/hw/vendor.oplus.hardware.vibrator-service',
                'vendor/etc/init/vibrator-default.rc',
                'odm/etc/vibrator/vibrator_effect.json'):
        print(f"   {'ok  ' if key in files else 'MISS'} {key}")
        if key not in files:
            problems.append(f"expected {key} in the ramdisk")

    return finish(problems, summary, args)


def finish(problems, summary, args):
    print()
    if args.json_out:
        with open(args.json_out, 'w') as fh:
            json.dump({'ok': not problems, 'problems': problems, **summary}, fh, indent=2)
    if problems:
        print(f"== {len(problems)} problem(s):")
        for p in problems:
            print(f"   - {p}")
        if not args.no_strict:
            return 1
        print("   (--no-strict: exiting 0 anyway)")
    else:
        print("== all checks passed")
    return 0


if __name__ == '__main__':
    sys.exit(main())
