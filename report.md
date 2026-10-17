# OrangeFox fox_16.0 build report - OnePlus Ace 5 (OP5D2BL1)

- run: #3 (attempt 1) -> **success**
- event: `push` on `refs/heads/OrangeFox`
- date: 2026-10-17T04:29:42Z
- device tree: `https://github.com/XiaoChen515144/OnePlus-Ace5@12471a2217c09d56df8fe7b2ae1e8f1e3311816c`
- lunch: `twrp_OP5D2BL1-bp2a-eng` | targets: `adbd recoveryimage` | type: `Alpha`
- runner: 4 vCPU, 15 GiB RAM

## image
-rw-r--r-- 1 runner runner 104857600 Oct 17 04:28 /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.img
-rw-r--r-- 1 runner runner 104857600 Oct 17 04:28 /fox-work/out/target/product/OP5D2BL1/recovery.img
92618162996e116a78af53ad675d18543b4fa94fd43e8246b869df974df5ece2  /fox-work/out/target/product/OP5D2BL1/recovery.img

## image self-check
{
  "ok": true,
  "problems": [],
  "header_version": 4,
  "ramdisk_size_compressed": 68876441,
  "ramdisk_size_uncompressed": 186861056,
  "avb": true,
  "avb_magic": "AVB0",
  "avb_vbmeta_offset": 68882432,
  "cpio_entries": 5012,
  "cpio_files": 5012,
  "kernel_modules": 483,
  "vibration_files": 107,
  "modules_load_recovery": 456,
  "modules_load_recovery_missing": [],
  "device_tree_files": 829,
  "device_tree_missing": [],
  "device_tree_content_mismatch": []
}
## image self-check output
== image: /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.img
   size: 104,857,600 bytes
   header v4, header_size 1584, kernel 0, ramdisk 68,876,441
   cmdline: ''
   lz4 legacy: 23 blocks -> 186,861,056 bytes cpio
   avb hash footer: AVB0 at 68,882,432 (832 B)
== ramdisk: 5,012 entries (4,787 files, 225 symlinks)
   kernel modules: 483
   vibration related: 107
   modules.load.recovery: 456 entries, 0 missing
   device tree recovery/root: 829 files, 0 missing
   content check: 829 compared, 0 differ
   ok   system/bin/recovery
   ok   system/bin/twrp
   ok   system/etc/twrp.flags
   ok   vendor/bin/hw/vendor.oplus.hardware.vibrator-service
   ok   vendor/etc/init/vibrator-default.rc
   ok   odm/etc/vibrator/vibrator_effect.json

== all checks passed

## ldcheck (missing dynamic dependencies)
### ldcheck vendor/bin/qseecomd
readelf: Warning: Separate debug info file /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libc.so found, but CRC does not match - ignoring
libs: ['vendor/bin/qseecomd', 'system/lib64/libcutils.so', 'system/lib64/libutils.so', 'system/lib64/liblog.so', 'vendor/lib64/libQSEEComAPI.so', 'vendor/lib64/libdrmfs.so', 'vendor/lib64/libminkdescriptor.so', 'vendor/lib64/libdmabufheap.so', 'system/lib64/libc++.so', 'system/lib64/libc.so', 'system/lib64/libm.so', 'system/lib64/libdl.so', 'system/lib64/libbase.so', 'system/lib64/libvndksupport.so', 'vendor/lib64/libqcbor.so', 'vendor/lib64/libdiag.so', 'system/lib64/libxml2.so', 'system/lib64/ld-android.so', 'system/lib64/libdl_android.so', 'system/lib64/libandroidicu.so', 'system/lib64/libicuuc.so', 'system/lib64/libicui18n.so']
unused: {'vendor/lib64/libQSEEComAPI.so', 'vendor/lib64/libdrmfs.so', 'system/lib64/libicuuc.so', 'system/lib64/libicui18n.so', 'system/lib64/libxml2.so', 'system/lib64/libdl_android.so', 'vendor/lib64/libdiag.so', 'system/lib64/libvndksupport.so', 'system/lib64/libm.so', 'system/lib64/libandroidicu.so', 'system/lib64/libutils.so'}
### ldcheck vendor/bin/hw/vendor.oplus.hardware.vibrator-service
readelf: Warning: Separate debug info file /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libc.so found, but CRC does not match - ignoring
libs: ['vendor/bin/hw/vendor.oplus.hardware.vibrator-service', 'system/lib64/android.hardware.vibrator-V2-ndk.so', 'vendor/lib64/vendor.aac.hardware.richtap.vibrator-V2-ndk.so', 'vendor/lib64/vendor.oplus.hardware.vibrator-V1-ndk.so', 'vendor/lib64/vendor.oplus.hardware.oplusvibrator-V2-ndk.so', 'vendor/lib64/libsoc_helper.so', 'system/lib64/libcutils.so', 'system/lib64/libutils.so', 'system/lib64/libbase.so', 'vendor/lib64/liboplusvibratoreffect.so', 'system/lib64/libbinder_ndk.so', 'vendor/lib64/libaacvibrator.so', 'vendor/lib64/libsivibrator.so', 'vendor/lib64/libtfavib.so', 'system/lib64/liblog.so', 'system/lib64/libc++.so', 'system/lib64/libc.so', 'system/lib64/libm.so', 'system/lib64/libdl.so', 'system/lib64/libvndksupport.so', 'system/lib64/libjsoncpp.so', 'system/lib64/libbinder.so', 'system/lib64/ld-android.so', 'system/lib64/libdl_android.so', 'system/lib64/libapexsupport.so']
unused: {'vendor/lib64/vendor.oplus.hardware.vibrator-V1-ndk.so', 'system/lib64/libbase.so'}
### ldcheck vendor/bin/hw/android.hardware.security.keymint-service-qti
readelf: Warning: Separate debug info file /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libc.so found, but CRC does not match - ignoring
libs: ['vendor/bin/hw/android.hardware.security.keymint-service-qti', 'system/lib64/liblog.so', 'system/lib64/libcutils.so', 'system/lib64/libbase.so', 'system/lib64/libutils.so', 'system/lib64/libhardware.so', 'system/lib64/libbinder_ndk.so', 'system/lib64/libhidlbase.so', 'system/lib64/android.hardware.keymaster@4.0.so', 'vendor/lib64/libqtikeymint.so', 'system/lib64/libcrypto.so', 'system/lib64/android.hardware.security.keymint-V3-ndk.so', 'system/lib64/android.hardware.security.rkp-V3-ndk.so', 'system/lib64/android.hardware.security.secureclock-V1-ndk.so', 'system/lib64/android.hardware.security.sharedsecret-V1-ndk.so', 'system/lib64/libc++.so', 'system/lib64/libc.so', 'system/lib64/libm.so', 'system/lib64/libdl.so', 'system/lib64/libvndksupport.so', 'system/lib64/libbinder.so', 'system/lib64/android.hardware.keymaster@3.0.so', 'vendor/lib64/libkeymasterdeviceutils.so', 'vendor/lib64/libqcbor.so', 'system/lib64/libkeymaster_messages.so', 'system/lib64/android.hardware.keymaster@4.1.so', 'vendor/lib64/libkeymasterutils.so', 'system/lib64/ld-android.so', 'system/lib64/libdl_android.so', 'system/lib64/libapexsupport.so', 'vendor/lib64/libion.so', 'vendor/lib64/libdmabufheap.so', 'vendor/lib64/libminkdescriptor.so', 'vendor/lib64/libQSEEComAPI.so']
unused: {'system/lib64/libbase.so', 'system/lib64/libm.so', 'system/lib64/libhidlbase.so', 'system/lib64/android.hardware.keymaster@4.0.so', 'system/lib64/android.hardware.keymaster@3.0.so', 'system/lib64/android.hardware.keymaster@4.1.so', 'vendor/lib64/libion.so', 'system/lib64/libhardware.so'}
### ldcheck vendor/bin/hw/android.hardware.weaver-service.nxp
readelf: Warning: Separate debug info file /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libc.so found, but CRC does not match - ignoring
libs: ['vendor/bin/hw/android.hardware.weaver-service.nxp', 'system/lib64/android.hardware.weaver-V2-ndk.so', 'system/lib64/libbase.so', 'system/lib64/libbinder_ndk.so', 'system/lib64/liblog.so', 'vendor/lib64/ese_weaver.so', 'vendor/lib64/vendor.oplus.hardware.weaver-V1-ndk.so', 'system/lib64/libc++.so', 'system/lib64/libc.so', 'system/lib64/libm.so', 'system/lib64/libdl.so', 'system/lib64/libbinder.so', 'system/lib64/libutils.so', 'vendor/lib64/android.se.omapi-V1-ndk.so', 'system/lib64/libcutils.so', 'vendor/lib64/libjc_keymint_transport_nxp.so', 'system/lib64/libhardware.so', 'system/lib64/libhidlbase.so', 'system/lib64/ld-android.so', 'system/lib64/libapexsupport.so', 'system/lib64/libvndksupport.so', 'vendor/lib64/android.hardware.secure_element@1.0.so', 'vendor/lib64/android.hardware.secure_element@1.1.so', 'vendor/lib64/android.hardware.secure_element@1.2.so', 'system/lib64/libdl_android.so']
unused: {'system/lib64/libm.so', 'system/lib64/libbase.so', 'system/lib64/libhardware.so'}
### ldcheck vendor/bin/hw/android.hardware.secure_element-service.qti
readelf: Warning: Separate debug info file /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libc.so found, but CRC does not match - ignoring
libs: ['vendor/bin/hw/android.hardware.secure_element-service.qti', 'vendor/lib64/libQSEEComAPI.so', 'vendor/lib64/hw/libEseUtils.so', 'vendor/lib64/libGPQeSE.so', 'system/lib64/libbase.so', 'system/lib64/liblog.so', 'system/lib64/libutils.so', 'system/lib64/libbinder_ndk.so', 'vendor/lib64/android.hardware.secure_element-V1-ndk.so', 'system/lib64/libc++.so', 'system/lib64/libc.so', 'system/lib64/libm.so', 'system/lib64/libdl.so', 'vendor/lib64/libdmabufheap.so', 'vendor/lib64/libqcbor.so', 'vendor/lib64/libminkdescriptor.so', 'system/lib64/libhidlbase.so', 'system/lib64/libhardware.so', 'system/lib64/libcutils.so', 'vendor/lib64/android.hardware.secure_element@1.0.so', 'vendor/lib64/libGPTEE_vendor.so', 'system/lib64/libvndksupport.so', 'system/lib64/libbinder.so', 'system/lib64/ld-android.so', 'system/lib64/libdl_android.so', 'system/lib64/libapexsupport.so']
unused: {'vendor/lib64/android.hardware.secure_element@1.0.so', 'system/lib64/libhardware.so', 'system/lib64/libm.so', 'system/lib64/libhidlbase.so'}

## product output
total 467184
drwxr-xr-x  2 runner runner      4096 Oct 17 04:28 FOX_AIK
-rw-r--r--  1 runner runner 104857600 Oct 17 04:28 OrangeFox-R12.0-Alpha-OP5D2BL1.img
-rw-r--r--  1 runner runner       107 Oct 17 04:28 OrangeFox-R12.0-Alpha-OP5D2BL1.img.md5
-rw-r--r--  1 runner runner  80960370 Oct 17 04:29 OrangeFox-R12.0-Alpha-OP5D2BL1.zip
-rw-r--r--  1 runner runner       107 Oct 17 04:29 OrangeFox-R12.0-Alpha-OP5D2BL1.zip.md5
-rw-r--r--  1 runner runner   1686576 Oct 17 03:26 all_modules.txt
-rw-r--r--  1 runner runner         1 Oct 17 04:23 android-info.txt
drwxr-xr-x  3 runner runner      4096 Oct 17 04:28 apex
-rw-r--r--  1 runner runner        84 Oct 17 03:09 build_fingerprint.txt
-rw-r--r--  1 runner runner        53 Oct 17 03:25 build_thumbprint.txt
-rw-r--r--  1 runner runner    156951 Oct 17 03:25 clean_steps.mk
drwxr-xr-x  2 runner runner      4096 Oct 17 04:23 debug_ramdisk
drwxr-xr-x  2 runner runner      4096 Oct 17 04:27 fake_packages
-rw-r--r--  1 runner runner       143 Oct 17 04:28 installed-files-ramdisk.json
-rw-r--r--  1 runner runner        28 Oct 17 04:28 installed-files-ramdisk.txt
drwxr-xr-x  9 runner runner      4096 Oct 17 04:22 obj
drwxr-xr-x  3 runner runner      4096 Oct 17 04:27 odm
-rw-r--r--  1 runner runner        43 Oct 17 03:26 previous_build_config.mk
-rw-r--r--  1 runner runner         0 Oct 17 03:26 previous_use_partial_compile.txt
drwxr-xr-x  3 runner runner      4096 Oct 17 04:27 product
drwxr-xr-x  9 runner runner      4096 Oct 17 04:28 ramdisk
-rw-r--r--  1 runner runner 186861056 Oct 17 04:28 ramdisk-recovery.cpio
-rw-r--r--  1 runner runner  68876441 Oct 17 04:28 ramdisk-recovery.img
-rw-r--r--  1 runner runner   1962690 Oct 17 04:28 ramdisk.img
drwxr-xr-x  3 runner runner      4096 Oct 17 03:10 recovery
-rw-r--r--  1 runner runner 104857600 Oct 17 04:28 recovery.img
drwxr-xr-x 27 runner runner      4096 Oct 17 04:28 root
drwxr-xr-x  9 runner runner      4096 Oct 17 04:29 symbols
drwxr-xr-x  6 runner runner      4096 Oct 17 04:28 system

## kernel module loading
(no matches)

## haptics / vibrator
16071:[ 63% 15631/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-cpp clang++ android/hardware/vibrator/Effect.cpp (priority: 12)
16072:[ 63% 15632/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-cpp clang++ android/hardware/vibrator/EffectStrength.cpp (priority: 12)
16076:[ 63% 15636/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-ndk clang++ android/hardware/vibrator/CompositePrimitive.cpp (priority: 12)
16077:[ 63% 15637/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-ndk clang++ android/hardware/vibrator/Effect.cpp (priority: 12)
16078:[ 63% 15638/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-cpp clang++ android/hardware/vibrator/CompositeEffect.cpp (priority: 12)
16079:[ 63% 15639/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-ndk clang++ android/hardware/vibrator/EffectStrength.cpp (priority: 12)
16080:[ 63% 15640/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-cpp clang++ android/hardware/vibrator/IVibratorCallback.cpp (priority: 12)
16081:[ 63% 15641/24624] //hardware/interfaces/vibrator/1.1:android.hardware.vibrator@1.1 generate toc android.hardware.vibrator@1.1.so (priority: 12)
16082:[ 63% 15642/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-ndk clang++ android/hardware/vibrator/CompositeEffect.cpp (priority: 12)
16083:[ 63% 15643/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-cpp clang++ android/hardware/vibrator/IVibrator.cpp (priority: 12)
16086:[ 63% 15646/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-ndk clang++ android/hardware/vibrator/IVibratorCallback.cpp (priority: 12)
16087:[ 63% 15647/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-ndk clang++ android/hardware/vibrator/IVibrator.cpp (priority: 12)
16088:[ 63% 15648/24624] //hardware/interfaces/vibrator/1.2:android.hardware.vibrator@1.2 clang++ android/hardware/vibrator/1.2/types.cpp (priority: 12)
16093:[ 63% 15653/24624] //hardware/interfaces/vibrator/1.2:android.hardware.vibrator@1.2 clang++ android/hardware/vibrator/1.2/VibratorAll.cpp (priority: 12)
19519:[ 69% 17072/24624] target Prebuilt: android.hardware.vibrator@1.0 (/fox-work/out/target/product/OP5D2BL1/obj/SHARED_LIBRARIES/android.hardware.vibrator@1.0_intermediates/android.hardware.vibrator@1.0.so) (priority: 11)
19520:[ 69% 17073/24624] Copy symbols with mapping: /fox-work/out/target/product/OP5D2BL1/symbols/system/lib64/android.hardware.vibrator-V2-cpp.so (priority: 11)
19521:[ 69% 17074/24624] Copy symbols with mapping: /fox-work/out/target/product/OP5D2BL1/symbols/system/lib64/android.hardware.vibrator-V2-ndk.so (priority: 11)
19523:[ 69% 17076/24624] Copy symbols with mapping: /fox-work/out/target/product/OP5D2BL1/symbols/system/lib64/android.hardware.vibrator@1.1.so (priority: 11)
19619:[ 69% 17168/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-cpp link android.hardware.vibrator-V1-cpp.so (priority: 11)
19624:[ 69% 17173/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-ndk link android.hardware.vibrator-V1-ndk.so (priority: 11)
19633:[ 69% 17180/24624] //hardware/interfaces/vibrator/1.2:android.hardware.vibrator@1.2 link android.hardware.vibrator@1.2.so (priority: 11)
24486:[ 89% 22033/24624] target Prebuilt: android.hardware.vibrator-V2-cpp (/fox-work/out/target/product/OP5D2BL1/obj/SHARED_LIBRARIES/android.hardware.vibrator-V2-cpp_intermediates/android.hardware.vibrator-V2-cpp.so) (priority: 10)
24487:[ 89% 22034/24624] Copy symbols with mapping: /fox-work/out/target/product/OP5D2BL1/symbols/system/lib64/android.hardware.vibrator-V1-cpp.so (priority: 10)
24488:[ 89% 22035/24624] Copy symbols with mapping: /fox-work/out/target/product/OP5D2BL1/symbols/system/lib64/android.hardware.vibrator-V1-ndk.so (priority: 10)
24489:[ 89% 22036/24624] target Prebuilt: android.hardware.vibrator-V2-ndk (/fox-work/out/target/product/OP5D2BL1/obj/SHARED_LIBRARIES/android.hardware.vibrator-V2-ndk_intermediates/android.hardware.vibrator-V2-ndk.so) (priority: 10)
24490:[ 89% 22037/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/lib64/android.hardware.vibrator@1.0.so (priority: 10)
24491:[ 89% 22038/24624] target Prebuilt: android.hardware.vibrator@1.1 (/fox-work/out/target/product/OP5D2BL1/obj/SHARED_LIBRARIES/android.hardware.vibrator@1.1_intermediates/android.hardware.vibrator@1.1.so) (priority: 10)
24493:[ 89% 22040/24624] Copy symbols with mapping: /fox-work/out/target/product/OP5D2BL1/symbols/system/lib64/android.hardware.vibrator@1.2.so (priority: 10)
24692:[ 90% 22182/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-cpp strip android.hardware.vibrator-V1-cpp.so (priority: 10)
24693:[ 90% 22183/24624] //hardware/interfaces/vibrator/aidl:android.hardware.vibrator-V1-ndk strip android.hardware.vibrator-V1-ndk.so (priority: 10)
24702:[ 90% 22185/24624] //hardware/interfaces/vibrator/1.2:android.hardware.vibrator@1.2 strip android.hardware.vibrator@1.2.so (priority: 10)
24946:[ 91% 22427/24624] target Prebuilt: android.hardware.vibrator-V1-cpp (/fox-work/out/target/product/OP5D2BL1/obj/SHARED_LIBRARIES/android.hardware.vibrator-V1-cpp_intermediates/android.hardware.vibrator-V1-cpp.so) (priority: 9)
24947:[ 91% 22428/24624] target Prebuilt: android.hardware.vibrator-V1-ndk (/fox-work/out/target/product/OP5D2BL1/obj/SHARED_LIBRARIES/android.hardware.vibrator-V1-ndk_intermediates/android.hardware.vibrator-V1-ndk.so) (priority: 9)
24948:[ 91% 22429/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/lib64/android.hardware.vibrator-V2-cpp.so (priority: 9)
24949:[ 91% 22430/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/lib64/android.hardware.vibrator-V2-ndk.so (priority: 9)
24950:[ 91% 22431/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/lib64/android.hardware.vibrator@1.1.so (priority: 9)
24951:[ 91% 22432/24624] target Prebuilt: android.hardware.vibrator@1.2 (/fox-work/out/target/product/OP5D2BL1/obj/SHARED_LIBRARIES/android.hardware.vibrator@1.2_intermediates/android.hardware.vibrator@1.2.so) (priority: 9)
26594:[ 97% 24075/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/lib64/android.hardware.vibrator-V1-ndk.so (priority: 8)
26595:[ 97% 24076/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/lib64/android.hardware.vibrator-V1-cpp.so (priority: 8)
26596:[ 97% 24077/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/lib64/android.hardware.vibrator@1.2.so (priority: 8)

## ninja progress when it stopped
[100% 24624/24624]
failed targets: 0
0

## build errors
976:[  3% 929/24624] //external/rust/android-crates-io/crates/thiserror:libthiserror rustc src/lib.rs [linux_glibc] (priority: 58)
1079:[  4% 1032/24624] //external/rust/android-crates-io/crates/thiserror:libthiserror rustc src/lib.rs (priority: 52)
17825:  915 |         test_syntax_error (_("syntax error: `%s' unexpected"), argv[pos]);
18084: 6261 |           msg = EOF_Reached ? _("syntax error: unexpected end of file") : _("syntax error");

## out/error.log

## errors found in the combined step log
18264:  513 |   return (_(cmd_error_table[code]));
18438:   96 |   &print_shift_error,
18658:  147 |   test_syntax_error (_("argument expected"), (char *)NULL);
18667:  156 |   test_syntax_error (_("%s: integer expression expected"), pch);
18676:  265 |         test_syntax_error (_("`)' expected"), (char *)NULL);
18685:  267 |         test_syntax_error (_("`)' expected, found %s"), argv[pos]);
18694:  469 |       test_syntax_error (_("%s: binary operator expected"), w);
18703:  771 |         test_syntax_error (_("%s: unary operator expected"), argv[pos]);
18712:  774 |     test_syntax_error (_("%s: unary operator expected"), argv[pos]);
18721:  815 |     test_syntax_error (_("%s: binary operator expected"), argv[pos+1]);
18730:  897 |         test_syntax_error (_("missing `]'"), (char *)NULL);
18739:  915 |         test_syntax_error (_("syntax error: `%s' unexpected"), argv[pos]);
18748:  917 |         test_syntax_error (_("too many arguments"), (char *)NULL);
18887: 2924 |       report_syntax_error (_("maximum here-document count exceeded"));
18896:  210 | static void report_syntax_error PARAMS((char *));
18899: 4550 |       if (etext = error_token_from_token (cond_token))
18902: 4550 |       if (etext = error_token_from_token (cond_token))
18906: 4550 |       if (etext = error_token_from_token (cond_token))
18910: 4632 |           if (etext = error_token_from_token (cond_token))
18913: 4632 |           if (etext = error_token_from_token (cond_token))
18917: 4632 |           if (etext = error_token_from_token (cond_token))
18921: 4664 |           if (etext = error_token_from_token (tok))
18924: 4664 |           if (etext = error_token_from_token (tok))
18928: 4664 |           if (etext = error_token_from_token (tok))
18932: 4715 |           if (etext = error_token_from_token (tok))
18935: 4715 |           if (etext = error_token_from_token (tok))
18939: 4715 |           if (etext = error_token_from_token (tok))
18943: 4742 |           if (etext = error_token_from_token (tok))
18946: 4742 |           if (etext = error_token_from_token (tok))
18950: 4742 |           if (etext = error_token_from_token (tok))
18954: 4760 |       else if (etext = error_token_from_token (tok))
18957: 4760 |       else if (etext = error_token_from_token (tok))
18961: 4760 |       else if (etext = error_token_from_token (tok))
18998: 6261 |           msg = EOF_Reached ? _("syntax error: unexpected end of file") : _("syntax error");
19975:[ 67% 16627/24624] //external/libnl:libnl clang lib/error.c (priority: 12)
20107:[ 68% 16746/24624] //external/libxml2:libxml2 clang error.c (priority: 12)
26126:[ 92% 22693/24624] //system/libbase:libbase clang++ posix_strerror_r.cpp [linux_glibc x86] (priority: 9)
26144:[ 92% 22711/24624] //system/libbase:libbase clang++ errors_unix.cpp [linux_glibc x86] (priority: 9)
27162:[ 96% 23729/24624] //external/zstd:libzstd clang lib/common/error_private.c [apex31] (priority: 9)
27198:[ 96% 23765/24624] //external/zstd:libzstd clang lib/common/error_private.c [linux_glibc] (priority: 9)

## disk / memory at the end of the job
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       146G  128G   19G  88% /
tmpfs           7.9G  172K  7.9G   1% /dev/shm
tmpfs           3.2G 1000K  3.2G   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
efivarfs        128M   34K  128M   1% /sys/firmware/efi/efivars
/dev/sda15      105M  6.1M   99M   6% /boot/efi
tmpfs           1.6G   12K  1.6G   1% /run/user/1001
               total        used        free      shared  buff/cache   available
Mem:            15Gi       648Mi       3.9Gi        37Mi        11Gi        14Gi
Swap:           10Gi       187Mi        10Gi
76G	/fox-work/fox_16.0
13G	/fox-work/out

## last 500 build log lines
[ 98% 24218/24624] //system/core/libasyncio:libasyncio static link libasyncio.a [linux_glibc] (priority: 8)
[ 98% 24219/24624] //external/avb:libavb static link libavb.a [linux_glibc] (priority: 8)
[ 98% 24220/24624] //external/avb:libavb static link libavb.a [linux_glibc x86] (priority: 8)
[ 98% 24221/24624] //system/libbase:libbase static link libbase.a [linux_glibc x86] (priority: 8)
[ 98% 24222/24624] //external/brotli:libbrotli static link libbrotli.a [linux_glibc] (priority: 8)
[ 98% 24223/24624] //build/soong/cc/libbuildversion:libbuildversion static link libbuildversion.a [apex31] (priority: 8)
[ 98% 24224/24624] //external/brotli:libbrotli static link libbrotli.a [apex31] (priority: 8)
[ 98% 24225/24624] //build/soong/cc/libbuildversion:libbuildversion static link libbuildversion.a [linux_glibc] (priority: 8)
[ 98% 24226/24624] //external/libcap:libcap static link libcap.a [apex31] (priority: 8)
[ 98% 24227/24624] //prebuilts/clang/host/linux-x86:libc++ generate toc libc++.so [linux_glibc x86] (priority: 8)
[ 98% 24228/24624] //external/boringssl:libcrypto generate toc libcrypto.so [apex31] (priority: 8)
[ 98% 24229/24624] //external/boringssl:libcrypto static link libcrypto.a [linux_glibc x86] (priority: 8)
[ 98% 24230/24624] //external/boringssl:libcrypto_static static link libcrypto_static.a [linux_glibc] (priority: 8)
[ 98% 24231/24624] //system/core/libcrypto_utils:libcrypto_utils static link libcrypto_utils.a [apex31] (priority: 8)
[ 98% 24232/24624] //system/core/libcrypto_utils:libcrypto_utils static link libcrypto_utils.a [linux_glibc] (priority: 8)
[ 98% 24233/24624] //system/core/libcrypto_utils:libcrypto_utils static link libcrypto_utils.a [linux_glibc x86] (priority: 8)
[ 98% 24234/24624] //system/core/libcutils:libcutils_sockets static link libcutils_sockets.a [apex31] (priority: 8)
[ 98% 24235/24624] //system/core/diagnose_usb:libdiagnose_usb static link libdiagnose_usb.a [apex31] (priority: 8)
[ 98% 24236/24624] //system/core/diagnose_usb:libdiagnose_usb static link libdiagnose_usb.a [linux_glibc] (priority: 8)
[ 98% 24237/24624] //system/extras/ext4_utils:libext4_utils static link libext4_utils.a [linux_glibc] (priority: 8)
[ 98% 24238/24624] //system/extras/ext4_utils:libext4_utils static link libext4_utils.a [linux_glibc x86] (priority: 8)
[ 98% 24239/24624] //system/extras/libfec:libfec static link libfec.a [linux_glibc] (priority: 8)
[ 98% 24240/24624] //system/extras/libfec:libfec static link libfec.a [linux_glibc x86] (priority: 8)
[ 98% 24241/24624] //external/fec:libfec_rs static link libfec_rs.a [linux_glibc] (priority: 8)
[ 98% 24242/24624] //external/fec:libfec_rs static link libfec_rs.a [linux_glibc x86] (priority: 8)
[ 98% 24243/24624] //packages/modules/adb:adbd clang++ daemon/main.cpp [apex31] (priority: 8)
[ 98% 24244/24624] //system/logging/liblog:liblog static link liblog.a [linux_glibc x86] (priority: 8)
[ 98% 24245/24624] //external/lz4/lib:liblz4 static link liblz4.a [apex31] (priority: 8)
[ 98% 24246/24624] //external/mdnsresponder:libmdnssd static link libmdnssd.a [linux_glibc] (priority: 8)
[ 98% 24247/24624] //external/mdnsresponder:libmdnssd static link libmdnssd.a [apex31] (priority: 8)
[ 98% 24248/24624] //external/minijail:libminijail static link libminijail.a [linux_glibc] (priority: 8)
[ 98% 24249/24624] //packages/modules/adb:adbd clang++ daemon/main.cpp [linux_glibc] (priority: 8)
[ 98% 24250/24624] //external/minijail:libminijail static link libminijail.a [apex31] (priority: 8)
[ 98% 24251/24624] //system/core/libsparse:libsparse static link libsparse.a [linux_glibc] (priority: 8)
[ 98% 24252/24624] //system/core/libsparse:libsparse static link libsparse.a [linux_glibc x86] (priority: 8)
[ 98% 24253/24624] //system/core/libprocessgroup:libprocessgroup generate toc libprocessgroup.so [apex31] (priority: 8)
[ 98% 24254/24624] //external/selinux/libselinux:libselinux generate toc libselinux.so (priority: 8)
[ 98% 24255/24624] //system/extras/squashfs_utils:libsquashfs_utils static link libsquashfs_utils.a [linux_glibc] (priority: 8)
[ 98% 24256/24624] //external/protobuf:libprotobuf-cpp-lite static link libprotobuf-cpp-lite.a [apex31] (priority: 8)
[ 98% 24257/24624] //system/extras/squashfs_utils:libsquashfs_utils static link libsquashfs_utils.a [linux_glibc x86] (priority: 8)
[ 98% 24258/24624] //external/zlib:libz static link libz.a [linux_glibc x86] (priority: 8)
[ 98% 24259/24624] //external/boringssl:libssl static link libssl.a [linux_glibc] (priority: 8)
[ 98% 24260/24624] //external/zstd:libzstd static link libzstd.a [linux_glibc] (priority: 8)
[ 98% 24261/24624] //external/zstd:libzstd static link libzstd.a [apex31] (priority: 8)
[ 98% 24262/24624] //system/sepolicy/contexts:odm_property_contexts.recovery building contexts: odm_property_contexts.recovery (priority: 8)
[ 98% 24263/24624] //external/boringssl:libssl static link libssl.a [apex31] (priority: 8)
[ 98% 24264/24624] //system/sepolicy/contexts:plat_property_contexts.recovery building contexts: plat_property_contexts.recovery (priority: 8)
[ 98% 24265/24624] //system/sepolicy/contexts:plat_file_contexts.recovery building contexts: plat_file_contexts.recovery (priority: 8)
[ 98% 24266/24624] //system/sepolicy/contexts:plat_service_contexts.recovery building contexts: plat_service_contexts.recovery (priority: 8)
[ 98% 24267/24624] //system/sepolicy/contexts:product_property_contexts.recovery building contexts: product_property_contexts.recovery (priority: 8)
[ 98% 24268/24624] //system/sepolicy/contexts:product_file_contexts.recovery building contexts: product_file_contexts.recovery (priority: 8)
[ 98% 24269/24624] //system/sepolicy/contexts:product_service_contexts.recovery building contexts: product_service_contexts.recovery (priority: 8)
[ 98% 24270/24624] //system/sepolicy/contexts:system_ext_file_contexts.recovery building contexts: system_ext_file_contexts.recovery (priority: 8)
[ 98% 24271/24624] //system/sepolicy/contexts:system_ext_property_contexts.recovery building contexts: system_ext_property_contexts.recovery (priority: 8)
[ 98% 24272/24624] //system/sepolicy/contexts:system_ext_service_contexts.recovery building contexts: system_ext_service_contexts.recovery (priority: 8)
[ 98% 24273/24624] //external/mksh:sh.recovery strip sh (priority: 8)
[ 98% 24274/24624] //system/sepolicy/contexts:vendor_property_contexts.recovery building contexts: vendor_property_contexts.recovery (priority: 8)
[ 98% 24275/24624] //system/sepolicy/contexts:odm_file_contexts.recovery building contexts: odm_file_contexts.recovery (priority: 8)
[ 98% 24276/24624] //system/sepolicy/contexts:vendor_service_contexts.recovery building contexts: vendor_service_contexts.recovery (priority: 8)
[ 98% 24277/24624] Install: /fox-work/out/target/product/OP5D2BL1/odm/etc/build.prop (priority: 7)
[ 98% 24278/24624] Install: /fox-work/out/target/product/OP5D2BL1/product/etc/build.prop (priority: 7)
[ 98% 24279/24624] //system/sepolicy/contexts:vendor_file_contexts.recovery building contexts: vendor_file_contexts.recovery (priority: 8)
[ 98% 24280/24624] //system/core/watchdogd:watchdogd.recovery strip watchdogd (priority: 8)
[ 98% 24281/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/relink_vendor_hw_binaries-timestamp (priority: 7)
[ 98% 24282/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/toybox (priority: 7)
[ 98% 24283/24624] target Prebuilt: adbd.recovery (/fox-work/out/target/product/OP5D2BL1/obj/EXECUTABLES/adbd.recovery_intermediates/adbd) (priority: 7)
[ 98% 24284/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/bu (priority: 7)
[ 98% 24285/24624] target Prebuilt: charger.recovery (/fox-work/out/target/product/OP5D2BL1/obj/EXECUTABLES/charger.recovery_intermediates/charger) (priority: 7)
[ 98% 24286/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/fatlabel (priority: 7)
[ 98% 24287/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/fox (priority: 7)
[ 98% 24288/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/fsck.exfat (priority: 7)
[ 98% 24289/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/fsck.fat (priority: 7)
[ 98% 24290/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/toolbox (priority: 7)
[ 98% 24291/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/linker64 (priority: 7)
[ 98% 24292/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/magiskboot (priority: 7)
[ 98% 24293/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/me.twrp.twrpapp.apk (priority: 7)
[ 98% 24294/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/mkexfatfs (priority: 7)
[ 98% 24295/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/mkfs.fat (priority: 7)
[ 98% 24296/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/pigz (priority: 7)
[ 98% 24297/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/privapp-permissions-twrpapp.xml (priority: 7)
[ 98% 24298/24624] //system/extras/verity/fec:fec clang++ image.cpp [linux_glibc] (priority: 8)
[ 98% 24299/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/android.hardware.boot@1.0-service.rc (priority: 7)
[ 98% 24300/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/android.hardware.boot@1.1-service.rc (priority: 7)
[ 98% 24301/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/android.hardware.boot@1.2-service.rc (priority: 7)
[ 98% 24302/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/android.hardware.health@2.0-service.rc (priority: 7)
[ 98% 24303/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/hw/android.hardware.health@2.0-impl-2.1.so (priority: 7)
[ 98% 24304/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/android.hardware.health@2.1-service.rc (priority: 7)
[ 98% 24305/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/vendor/etc/vintf/manifest/android.hardware.health@2.1.xml (priority: 7)
[ 98% 24306/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/relink_binaries-timestamp (priority: 7)
[ 98% 24307/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/hwservicemanager.rc (priority: 7)
[ 98% 24308/24624] Install: /fox-work/out/target/product/OP5D2BL1/root/init.recovery.hlthchrg.rc (priority: 7)
[ 98% 24309/24624] Install: /fox-work/out/target/product/OP5D2BL1/root/init.recovery.ldconfig.rc (priority: 7)
[ 98% 24310/24624] Install: /fox-work/out/target/product/OP5D2BL1/root/init.recovery.logd.rc (priority: 7)
[ 98% 24311/24624] Install: /fox-work/out/target/product/OP5D2BL1/root/init.recovery.service.rc (priority: 7)
[ 98% 24312/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/keystore2.rc (priority: 7)
[ 98% 24313/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libadbd.so (priority: 7)
[ 98% 24314/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libadbd_services.so (priority: 7)
[ 98% 24315/24624] target Strip: recovery (/fox-work/out/target/product/OP5D2BL1/obj/EXECUTABLES/recovery_intermediates/recovery) (priority: 7)
[ 98% 24316/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/lib64/libresetprop.so (priority: 7)
[ 98% 24317/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libsync.so (priority: 7)
[ 98% 24318/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/lpdumpd.rc (priority: 7)
[ 98% 24319/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/mkshrc (priority: 7)
[ 98% 24320/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/bin/recovery-persist (priority: 7)
[ 98% 24321/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/twrp (priority: 7)
[ 98% 24322/24624] Install: /fox-work/out/target/product/OP5D2BL1/fake_packages/file_contexts_text-timestamp (priority: 7)
cp: Skipped dir '/fox-work/out/target/product/OP5D2BL1/system/etc//root': No such file or directory
cp: bad 'mkdir': No such file or directory
cp: bad '/fox-work/out/target/product/OP5D2BL1/system/etc/nano': No such file or directory
[ 98% 24323/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/resetprop (priority: 7)
[ 98% 24324/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/servicemanager.rc (priority: 7)
[ 98% 24325/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/bin/recovery-refresh (priority: 7)
[ 98% 24326/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/simg2img (priority: 7)
[ 98% 24327/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/etc/task_profiles.json (priority: 7)
[ 98% 24328/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/vndservicemanager.rc (priority: 7)
[ 98% 24329/24624] Install: /fox-work/out/target/product/OP5D2BL1/root/system/bin/tzdata_twrp-timestamp (priority: 7)
[ 98% 24330/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libkeystoreinfo.so (priority: 7)
[ 98% 24331/24624] target Prebuilt: sh.recovery (/fox-work/out/target/product/OP5D2BL1/obj/EXECUTABLES/sh.recovery_intermediates/sh) (priority: 7)
[ 98% 24332/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/twrp_ramdisk-timestamp (priority: 7)
[ 98% 24333/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/init/snapuserd.rc (priority: 7)
[ 98% 24334/24624] target Prebuilt: watchdogd.recovery (/fox-work/out/target/product/OP5D2BL1/obj/EXECUTABLES/watchdogd.recovery_intermediates/watchdogd) (priority: 7)
[ 98% 24335/24624] target Prebuilt: cgroups.recovery.json (/fox-work/out/target/product/OP5D2BL1/obj/ETC/cgroups.recovery.json_intermediates/cgroups.recovery.json) (priority: 7)
[ 98% 24336/24624] target Prebuilt: ld.config.recovery.txt (/fox-work/out/target/product/OP5D2BL1/obj/ETC/ld.config.recovery.txt_intermediates/ld.config.recovery.txt) (priority: 7)
[ 98% 24337/24624] Install: /fox-work/out/target/product/OP5D2BL1/system/build.prop (priority: 7)
[ 98% 24338/24624] Copy: /fox-work/out/target/product/OP5D2BL1/obj/ETC/init.environ.rc_intermediates/init.environ.rc (priority: 7)
[ 98% 24339/24624] Install: /fox-work/out/target/product/OP5D2BL1/system_ext/etc/build.prop (priority: 7)
[ 98% 24340/24624] Install: /fox-work/out/host/linux-x86/bin/lz4 (priority: 7)
[ 98% 24341/24624] Install: /fox-work/out/host/linux-x86/bin/mkbootfs (priority: 7)
[ 98% 24342/24624] host Prebuilt: libc++_32 (/fox-work/out/host/linux-x86/obj32/SHARED_LIBRARIES/libc++_intermediates/libc++.so) (priority: 7)
[ 98% 24343/24624] target Prebuilt: plat_file_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/plat_file_contexts.recovery_intermediates/plat_file_contexts.recovery) (priority: 7)
[ 98% 24344/24624] target Prebuilt: plat_service_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/plat_service_contexts.recovery_intermediates/plat_service_contexts.recovery) (priority: 7)
[ 98% 24345/24624] target Prebuilt: plat_property_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/plat_property_contexts.recovery_intermediates/plat_property_contexts.recovery) (priority: 7)
[ 98% 24346/24624] target Prebuilt: system_ext_file_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/system_ext_file_contexts.recovery_intermediates/system_ext_file_contexts.recovery) (priority: 7)
[ 98% 24347/24624] target Prebuilt: system_ext_service_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/system_ext_service_contexts.recovery_intermediates/system_ext_service_contexts.recovery) (priority: 7)
[ 98% 24348/24624] target Prebuilt: system_ext_property_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/system_ext_property_contexts.recovery_intermediates/system_ext_property_contexts.recovery) (priority: 7)
[ 98% 24349/24624] target Prebuilt: vendor_file_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/vendor_file_contexts.recovery_intermediates/vendor_file_contexts.recovery) (priority: 7)
[ 98% 24350/24624] target Prebuilt: vendor_service_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/vendor_service_contexts.recovery_intermediates/vendor_service_contexts.recovery) (priority: 7)
[ 98% 24351/24624] target Prebuilt: vendor_property_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/vendor_property_contexts.recovery_intermediates/vendor_property_contexts.recovery) (priority: 7)
[ 98% 24352/24624] Installed file list: /fox-work/out/target/product/OP5D2BL1/installed-files-ramdisk.txt (priority: 7)
[ 98% 24353/24624] target Prebuilt: odm_file_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/odm_file_contexts.recovery_intermediates/odm_file_contexts.recovery) (priority: 7)
[ 98% 24354/24624] target Prebuilt: odm_property_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/odm_property_contexts.recovery_intermediates/odm_property_contexts.recovery) (priority: 7)
[ 98% 24355/24624] target Prebuilt: product_file_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/product_file_contexts.recovery_intermediates/product_file_contexts.recovery) (priority: 7)
[ 98% 24356/24624] Building /fox-work/out/target/product/OP5D2BL1/vendor/build.prop (priority: 7)
[ 98% 24357/24624] target Prebuilt: product_service_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/product_service_contexts.recovery_intermediates/product_service_contexts.recovery) (priority: 7)
[ 98% 24358/24624] Install: /fox-work/out/host/linux-x86/bin/symbol_inject (priority: 7)
[ 98% 24359/24624] target Prebuilt: product_property_contexts.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/product_property_contexts.recovery_intermediates/product_property_contexts.recovery) (priority: 7)
[ 98% 24360/24624] //system/core/fs_mgr/libsnapshot/snapuserd:snapuserd link snapuserd (priority: 9)
[ 98% 24361/24624] Copy symbols with mapping: /fox-work/out/target/product/OP5D2BL1/symbols/recovery/root/system/bin/snapuserd (priority: 8)
[ 98% 24362/24624] //external/avb:avbtool Precompile the python sources of avbtool [linux_glibc] (priority: 7)
[ 98% 24363/24624] //system/core/fs_mgr/libsnapshot/snapuserd:snapuserd strip snapuserd (priority: 8)
[ 98% 24364/24624] target Prebuilt: snapuserd.recovery (/fox-work/out/target/product/OP5D2BL1/obj/EXECUTABLES/snapuserd.recovery_intermediates/snapuserd) (priority: 7)
[ 98% 24365/24624] //packages/modules/adb:adbd link adbd [linux_glibc] (priority: 7)
[ 98% 24366/24624] //system/tools/mkbootimg:mkbootimg python library archive [linux_glibc] (priority: 7)
[ 98% 24367/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/[ (priority: 6)
[ 98% 24368/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/acpi (priority: 6)
[ 98% 24369/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/adbd (priority: 6)
[ 98% 24370/24624] //system/extras/verity/fec:fec link fec32 [linux_glibc x86] (priority: 7)
[ 98% 24371/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/basename (priority: 6)
[ 98% 24372/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/base64 (priority: 6)
[ 98% 24373/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/blockdev (priority: 6)
[ 98% 24374/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/blkdiscard (priority: 6)
[ 98% 24375/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/brctl (priority: 6)
[ 98% 24376/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/cal (priority: 6)
[ 98% 24377/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/cat (priority: 6)
[ 99% 24378/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/charger (priority: 6)
[ 99% 24379/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/chattr (priority: 6)
[ 99% 24380/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/chcon (priority: 6)
[ 99% 24381/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/chgrp (priority: 6)
[ 99% 24382/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/chmod (priority: 6)
[ 99% 24383/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/chown (priority: 6)
[ 99% 24384/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/chroot (priority: 6)
[ 99% 24385/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/chrt (priority: 6)
[ 99% 24386/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/cksum (priority: 6)
[ 99% 24387/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/clear (priority: 6)
[ 99% 24388/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/cmp (priority: 6)
[ 99% 24389/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/comm (priority: 6)
[ 99% 24390/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/cp (priority: 6)
[ 99% 24391/24624] //system/extras/verity/fec:fec link fec [linux_glibc] (priority: 7)
[ 99% 24392/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/cpio (priority: 6)
[ 99% 24393/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/cut (priority: 6)
[ 99% 24394/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/date (priority: 6)
[ 99% 24395/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/dd (priority: 6)
[ 99% 24396/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/devmem (priority: 6)
[ 99% 24397/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/df (priority: 6)
[ 99% 24398/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/diff (priority: 6)
[ 99% 24399/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/dirname (priority: 6)
[ 99% 24400/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/dmesg (priority: 6)
[ 99% 24401/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/dos2unix (priority: 6)
[ 99% 24402/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/du (priority: 6)
[ 99% 24403/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/egrep (priority: 6)
[ 99% 24404/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/echo (priority: 6)
[ 99% 24405/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/env (priority: 6)
[ 99% 24406/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/expand (priority: 6)
[ 99% 24407/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/expr (priority: 6)
[ 99% 24408/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/fallocate (priority: 6)
[ 99% 24409/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/false (priority: 6)
[ 99% 24410/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/fgrep (priority: 6)
[ 99% 24411/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/find (priority: 6)
[ 99% 24412/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/file (priority: 6)
[ 99% 24413/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/flock (priority: 6)
[ 99% 24414/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/fmt (priority: 6)
[ 99% 24415/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/fsync (priority: 6)
[ 99% 24416/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/free (priority: 6)
[ 99% 24417/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/getconf (priority: 6)
[ 99% 24418/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/getenforce (priority: 6)
[ 99% 24419/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/getevent (priority: 6)
[ 99% 24420/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/getfattr (priority: 6)
[ 99% 24421/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/getopt (priority: 6)
[ 99% 24422/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/getprop (priority: 6)
[ 99% 24423/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/gpiodetect (priority: 6)
[ 99% 24424/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/gpioget (priority: 6)
[ 99% 24425/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/gpiofind (priority: 6)
[ 99% 24426/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/gpioinfo (priority: 6)
[ 99% 24427/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/gpioset (priority: 6)
[ 99% 24428/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/grep (priority: 6)
[ 99% 24429/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/groups (priority: 6)
[ 99% 24430/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/gunzip (priority: 6)
[ 99% 24431/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/gzip (priority: 6)
[ 99% 24432/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/head (priority: 6)
[ 99% 24433/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/hostname (priority: 6)
[ 99% 24434/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/i2cdetect (priority: 6)
[ 99% 24435/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/hwclock (priority: 6)
[ 99% 24436/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/i2cdump (priority: 6)
[ 99% 24437/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/i2cget (priority: 6)
[ 99% 24438/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/i2ctransfer (priority: 6)
[ 99% 24439/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/i2cset (priority: 6)
[ 99% 24440/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/iconv (priority: 6)
[ 99% 24441/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/ifconfig (priority: 6)
[ 99% 24442/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/id (priority: 6)
[ 99% 24443/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/inotifyd (priority: 6)
[ 99% 24444/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/insmod (priority: 6)
[ 99% 24445/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/install (priority: 6)
[ 99% 24446/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/ionice (priority: 6)
[ 99% 24447/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/iorenice (priority: 6)
[ 99% 24448/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/kill (priority: 6)
[ 99% 24449/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/linker_asan64 (priority: 6)
[ 99% 24450/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/killall (priority: 6)
[ 99% 24451/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/linker_hwasan64 (priority: 6)
[ 99% 24452/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/ln (priority: 6)
[ 99% 24453/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/log (priority: 6)
[ 99% 24454/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/load_policy (priority: 6)
[ 99% 24455/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/logger (priority: 6)
[ 99% 24456/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/losetup (priority: 6)
[ 99% 24457/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/logname (priority: 6)
[ 99% 24458/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/ls (priority: 6)
[ 99% 24459/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/lsmod (priority: 6)
[ 99% 24460/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/lsattr (priority: 6)
[ 99% 24461/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/lspci (priority: 6)
[ 99% 24462/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/lsof (priority: 6)
[ 99% 24463/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/md5sum (priority: 6)
[ 99% 24464/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/lsusb (priority: 6)
[ 99% 24465/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/memeater (priority: 6)
[ 99% 24466/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/microcom (priority: 6)
[ 99% 24467/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/mkdir (priority: 6)
[ 99% 24468/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/mkswap (priority: 6)
[ 99% 24469/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/mkfifo (priority: 6)
[ 99% 24470/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/mknod (priority: 6)
[ 99% 24471/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/mktemp (priority: 6)
[ 99% 24472/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/modinfo (priority: 6)
[ 99% 24473/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/modprobe (priority: 6)
[ 99% 24474/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/more (priority: 6)
[ 99% 24475/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/mountpoint (priority: 6)
[ 99% 24476/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/mount (priority: 6)
[ 99% 24477/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/mv (priority: 6)
[ 99% 24478/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/netcat (priority: 6)
[ 99% 24479/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/nc (priority: 6)
[ 99% 24480/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/netstat (priority: 6)
[ 99% 24481/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/nl (priority: 6)
[ 99% 24482/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/nice (priority: 6)
[ 99% 24483/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/nohup (priority: 6)
[ 99% 24484/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/nproc (priority: 6)
[ 99% 24485/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/nsenter (priority: 6)
[ 99% 24486/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/od (priority: 6)
[ 99% 24487/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/paste (priority: 6)
[ 99% 24488/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/patch (priority: 6)
[ 99% 24489/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/pgrep (priority: 6)
[ 99% 24490/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/pkill (priority: 6)
[ 99% 24491/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/pidof (priority: 6)
[ 99% 24492/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/pmap (priority: 6)
[ 99% 24493/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/printenv (priority: 6)
[ 99% 24494/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/printf (priority: 6)
[ 99% 24495/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/relink_libraries-timestamp (priority: 7)
[ 99% 24496/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/ps (priority: 6)
[ 99% 24497/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/pwd (priority: 6)
[ 99% 24498/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/readlink (priority: 6)
[ 99% 24499/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/readelf (priority: 6)
[ 99% 24500/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/realpath (priority: 6)
[ 99% 24501/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/renice (priority: 6)
[ 99% 24502/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/restorecon (priority: 6)
[ 99% 24503/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/rm (priority: 6)
[ 99% 24504/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/rmdir (priority: 6)
[ 99% 24505/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/rmmod (priority: 6)
[ 99% 24506/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/rtcwake (priority: 6)
[ 99% 24507/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/recovery (priority: 6)
[ 99% 24508/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sed (priority: 6)
[ 99% 24509/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/runcon (priority: 6)
[ 99% 24510/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sendevent (priority: 6)
[ 99% 24511/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/seq (priority: 6)
[ 99% 24512/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/setenforce (priority: 6)
[ 99% 24513/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/setfattr (priority: 6)
[ 99% 24514/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/setprop (priority: 6)
[ 99% 24515/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/setsid (priority: 6)
[ 99% 24516/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sh (priority: 6)
[ 99% 24517/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sha1sum (priority: 6)
[ 99% 24518/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sha224sum (priority: 6)
[ 99% 24519/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sha256sum (priority: 6)
[ 99% 24520/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sha384sum (priority: 6)
[ 99% 24521/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sha512sum (priority: 6)
[ 99% 24522/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sleep (priority: 6)
[ 99% 24523/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sort (priority: 6)
[ 99% 24524/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/split (priority: 6)
[ 99% 24525/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/snapuserd (priority: 6)
[ 99% 24526/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/start (priority: 6)
[ 99% 24527/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/stat (priority: 6)
[ 99% 24528/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/stop (priority: 6)
[ 99% 24529/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/strings (priority: 6)
[ 99% 24530/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/stty (priority: 6)
[ 99% 24531/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/swapoff (priority: 6)
[ 99% 24532/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sync (priority: 6)
[ 99% 24533/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/swapon (priority: 6)
[ 99% 24534/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sysctl (priority: 6)
[ 99% 24535/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tac (priority: 6)
[ 99% 24536/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tail (priority: 6)
[ 99% 24537/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/taskset (priority: 6)
[ 99% 24538/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tar (priority: 6)
[ 99% 24539/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/test (priority: 6)
[ 99% 24540/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tee (priority: 6)
[ 99% 24541/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/time (priority: 6)
[ 99% 24542/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/top (priority: 6)
[ 99% 24543/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/timeout (priority: 6)
[ 99% 24544/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/touch (priority: 6)
[ 99% 24545/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tr (priority: 6)
[ 99% 24546/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/true (priority: 6)
[ 99% 24547/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/truncate (priority: 6)
[ 99% 24548/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uclampset (priority: 6)
[ 99% 24549/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tty (priority: 6)
[ 99% 24550/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/umount (priority: 6)
[ 99% 24551/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/ulimit (priority: 6)
[ 99% 24552/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uniq (priority: 6)
[ 99% 24553/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uname (priority: 6)
[ 99% 24554/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/unix2dos (priority: 6)
[ 99% 24555/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/unlink (priority: 6)
[ 99% 24556/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uptime (priority: 6)
[ 99% 24557/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/unshare (priority: 6)
[ 99% 24558/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/usleep (priority: 6)
[ 99% 24559/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uudecode (priority: 6)
[ 99% 24560/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uuencode (priority: 6)
[ 99% 24561/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uuidgen (priority: 6)
[ 99% 24562/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/vi (priority: 6)
[ 99% 24563/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/vmstat (priority: 6)
[ 99% 24564/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/watch (priority: 6)
[ 99% 24565/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/watchdogd (priority: 6)
[ 99% 24566/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/which (priority: 6)
[ 99% 24567/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/wc (priority: 6)
[ 99% 24568/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/whoami (priority: 6)
[ 99% 24569/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/xargs (priority: 6)
[ 99% 24570/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/xxd (priority: 6)
[ 99% 24571/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/yes (priority: 6)
[ 99% 24572/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/zcat (priority: 6)
[ 99% 24573/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/cgroups.json (priority: 6)
[ 99% 24574/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/ld.config.txt (priority: 6)
[ 99% 24575/24624] Install: /fox-work/out/host/linux-x86/lib/libc++.so (priority: 6)
[ 99% 24576/24624] host Prebuilt: fec_32 (/fox-work/out/host/linux-x86/obj32/EXECUTABLES/fec_intermediates/fec32) (priority: 6)
[ 99% 24577/24624] host Prebuilt: fec (/fox-work/out/host/linux-x86/obj/EXECUTABLES/fec_intermediates/fec) (priority: 6)
[ 99% 24578/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/plat_file_contexts (priority: 6)
[ 99% 24579/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/plat_service_contexts (priority: 6)
[ 99% 24580/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/plat_property_contexts (priority: 6)
[ 99% 24581/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system_ext_file_contexts (priority: 6)
[ 99% 24582/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system_ext_service_contexts (priority: 6)
[ 99% 24583/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system_ext_property_contexts (priority: 6)
[ 99% 24584/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/vendor_file_contexts (priority: 6)
[ 99% 24585/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/vendor_service_contexts (priority: 6)
[ 99% 24586/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/vendor_property_contexts (priority: 6)
[ 99% 24587/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/odm_file_contexts (priority: 6)
[ 99% 24588/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/odm_property_contexts (priority: 6)
[ 99% 24589/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/product_file_contexts (priority: 6)
[ 99% 24590/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/product_service_contexts (priority: 6)
[ 99% 24591/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/product_property_contexts (priority: 6)
[ 99% 24592/24624] Install: /fox-work/out/target/product/OP5D2BL1/root/init.environ.rc (priority: 6)
[ 99% 24593/24624] Target recovery buildinfo: /fox-work/out/target/product/OP5D2BL1/recovery/root/prop.default (priority: 6)
[ 99% 24594/24624] //packages/modules/adb:adbd inject version symbol [linux_glibc] (priority: 6)
[ 99% 24595/24624] Install: /fox-work/out/host/linux-x86/bin/fec (priority: 5)
[ 99% 24596/24624] Install: /fox-work/out/host/linux-x86/bin/fec32 (priority: 5)
[ 99% 24597/24624] host Prebuilt: libadbd_auth (/fox-work/out/host/linux-x86/obj/SHARED_LIBRARIES/libadbd_auth_intermediates/libadbd_auth.so) (priority: 5)
[ 99% 24598/24624] host Prebuilt: libadbd_fs (/fox-work/out/host/linux-x86/obj/SHARED_LIBRARIES/libadbd_fs_intermediates/libadbd_fs.so) (priority: 5)
[ 99% 24599/24624] //external/avb:avbtool embedded python archive [linux_glibc] (priority: 6)
[ 99% 24600/24624] host Prebuilt: avbtool (/fox-work/out/host/linux-x86/obj/EXECUTABLES/avbtool_intermediates/avbtool) (priority: 5)
[ 99% 24601/24624] Install: /fox-work/out/host/linux-x86/bin/avbtool (priority: 4)
[ 99% 24602/24624] //system/tools/mkbootimg:mkbootimg Precompile the python sources of mkbootimg [linux_glibc] (priority: 6)
[ 99% 24603/24624] Install: /fox-work/out/host/linux-x86/lib64/libadbd_auth.so (priority: 4)
[ 99% 24604/24624] Install: /fox-work/out/host/linux-x86/lib64/libadbd_fs.so (priority: 4)
[ 99% 24605/24624] //packages/modules/adb:adbd strip adbd [linux_glibc] (priority: 5)
[ 99% 24606/24624] host Prebuilt: adbd (/fox-work/out/host/linux-x86/obj/EXECUTABLES/adbd_intermediates/adbd) (priority: 4)
[ 99% 24607/24624] //system/tools/mkbootimg:mkbootimg embedded python archive [linux_glibc] (priority: 5)
[ 99% 24608/24624] Install: /fox-work/out/host/linux-x86/bin/adbd (priority: 3)
[ 99% 24609/24624] host Prebuilt: mkbootimg (/fox-work/out/host/linux-x86/obj/EXECUTABLES/mkbootimg_intermediates/mkbootimg) (priority: 4)
[ 99% 24610/24624] Install: /fox-work/out/host/linux-x86/bin/mkbootimg (priority: 3)
[ 99% 24611/24624] Target ramdisk: /fox-work/out/target/product/OP5D2BL1/ramdisk.img (priority: 6)
[ 99% 24612/24624] //system/sepolicy:sepolicy.recovery Compiling cil files for sepolicy.recovery (priority: 8)
[ 99% 24613/24624] target Prebuilt: sepolicy.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/sepolicy.recovery_intermediates/sepolicy.recovery) (priority: 7)
[ 99% 24614/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/sepolicy (priority: 6)
[ 99% 24615/24624] build /fox-work/out/target/product/OP5D2BL1/obj/PACKAGING/recovery_intermediates/ramdisk_files-timestamp (priority: 5)
#########################################################################
Variables exported from build/core/Makefile:
FOX_VENDOR_CMD=Fox_Before_Recovery_Image FOX_MANIFEST_VER=16.0 BOARD_BOOT_HEADER_VERSION=4 TARGET_ARCH=arm64 TARGET_RECOVERY_ROOT_OUT=/fox-work/out/target/product/OP5D2BL1/recovery/root TARGET_VENDOR_RAMDISK_OUT=/fox-work/out/target/product/OP5D2BL1/vendor_ramdisk MKBOOTIMG=/fox-work/out/host/linux-x86/bin/mkbootimg MKBOOTFS=/fox-work/out/host/linux-x86/bin/mkbootfs INTERNAL_RECOVERYIMAGE_ARGS="--ramdisk /fox-work/out/target/product/OP5D2BL1/ramdisk-recovery.img  --pagesize 4096" INTERNAL_MKBOOTIMG_VERSION_ARGS=--os_version 99.87.36 --os_patch_level 2099-12-31 BOARD_MKBOOTIMG_ARGS="--header_version 4 --pagesize 4096" TARGET_OUT=/fox-work/out/target/product/OP5D2BL1/system COMPRESSION_COMMAND=/fox-work/out/host/linux-x86/bin/lz4 -l -12 --favor-decSpeed INSTALLED_RECOVERYIMAGE_TARGET=/fox-work/out/target/product/OP5D2BL1/recovery.img BOARD_BOOTIMAGE_PARTITION_SIZE= BOARD_RECOVERYIMAGE_PARTITION_SIZE=0x6400000 BOARD_USES_RECOVERY_AS_BOOT= INTERNAL_KERNEL_CMDLINE= BOARD_INCLUDE_RECOVERY_RAMDISK_IN_VENDOR_BOOT= BOARD_MOVE_RECOVERY_RESOURCES_TO_VENDOR_BOOT= ORANGEFOX_CALLING_CARD=2.0 recovery_ramdisk=/fox-work/out/target/product/OP5D2BL1/ramdisk-recovery.img
#########################################################################
-- The device is a virtual A/B device  - disabling the init.d addon .... 
Building OrangeFox...
-- Setting up environment variables
-- ARM64 arch detected. Copying ARM64 binaries
-- Symlinking "resetprop" ...
-- This build will use magiskboot for patching boot images ...
-- Backing up /fox-work/out/target/product/OP5D2BL1/recovery/root//sbin/magiskboot to: /tmp/fox_build_tmp/ ...
-- Copying bash ...
-- Replacing the "sh" applet with bash ...
-- Cleaning up any ash stragglers...
-- Copying nano editor ...
-- Copying the GNU "tar" binary (gnutar) ...
-- Copying the GNU "sed" binary (gnused) ...
-- Copying the OrangeFox InfoZip "zip" binary ...
-- Enabling the App Manager ...
-- Detected Magisk version: 30.7
-- Generating the build ID 
-- Saving some original file sizes 
-- Building the recovery image, using the official AOSP recovery image builder ...
[ 99% 24616/24624] ----- Making uncompressed recovery ramdisk ------ (priority: 4)
[ 99% 24617/24624] //packages/modules/adb:adbd link adbd [apex31] (priority: 7)
[ 99% 24618/24624] Copy symbols with mapping: /fox-work/out/target/product/OP5D2BL1/symbols/apex/com.android.adbd/bin/adbd (priority: 6)
[ 99% 24619/24624] //packages/modules/adb:adbd strip adbd [apex31] (priority: 6)
[ 99% 24620/24624] target Prebuilt: adbd.com.android.adbd (/fox-work/out/target/product/OP5D2BL1/obj/EXECUTABLES/adbd.com.android.adbd_intermediates/adbd) (priority: 5)
[ 99% 24621/24624] Install: /fox-work/out/target/product/OP5D2BL1/apex/com.android.adbd/bin/adbd (priority: 4)
[ 99% 24622/24624] ----- Making compressed recovery ramdisk ------ (priority: 3)
[ 99% 24623/24624] build /fox-work/out/target/product/OP5D2BL1/recovery.img (priority: 2)
[100% 24624/24624] build recoveryimage (priority: 1)
#########################################################################
Variables exported from build/core/Makefile:
FOX_VENDOR_CMD=Fox_After_Recovery_Image FOX_MANIFEST_VER=16.0 BOARD_BOOT_HEADER_VERSION=4 TARGET_ARCH=arm64 TARGET_RECOVERY_ROOT_OUT=/fox-work/out/target/product/OP5D2BL1/recovery/root TARGET_VENDOR_RAMDISK_OUT=/fox-work/out/target/product/OP5D2BL1/vendor_ramdisk MKBOOTIMG=/fox-work/out/host/linux-x86/bin/mkbootimg MKBOOTFS=/fox-work/out/host/linux-x86/bin/mkbootfs INTERNAL_RECOVERYIMAGE_ARGS="--ramdisk /fox-work/out/target/product/OP5D2BL1/ramdisk-recovery.img  --pagesize 4096" INTERNAL_MKBOOTIMG_VERSION_ARGS=--os_version 99.87.36 --os_patch_level 2099-12-31 BOARD_MKBOOTIMG_ARGS="--header_version 4 --pagesize 4096" TARGET_OUT=/fox-work/out/target/product/OP5D2BL1/system COMPRESSION_COMMAND=/fox-work/out/host/linux-x86/bin/lz4 -l -12 --favor-decSpeed INSTALLED_RECOVERYIMAGE_TARGET=/fox-work/out/target/product/OP5D2BL1/recovery.img INSTALLED_BOOTIMAGE_TARGET= BOARD_BOOTIMAGE_PARTITION_SIZE= BOARD_RECOVERYIMAGE_PARTITION_SIZE=0x6400000 BOARD_USES_RECOVERY_AS_BOOT= INTERNAL_KERNEL_CMDLINE= ORANGEFOX_CALLING_CARD=4.0 recovery_ramdisk=/fox-work/out/target/product/OP5D2BL1/ramdisk-recovery.img
#########################################################################
-- The device is a virtual A/B device  - disabling the init.d addon .... 
-- Setting up environment variables
-- This is a system-as-root build ...
-- Copying recovery: "/fox-work/out/target/product/OP5D2BL1/recovery.img" --> "/fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.img" 
-- Creating the OrangeFox zip installer ...
- Creating /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip for deployment ...
-- A/B device - copying magiskboot to zip installer ... 
-- Saving the vAB flag ... 
-- Deleting the initd addon ...
- Running ZIP command: zip --exclude=*.git* -r9 /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip .
  adding: recovery.img (deflated 45%)
  adding: META-INF/ (stored 0%)
  adding: META-INF/debug/ (stored 0%)
  adding: META-INF/debug/default.prop (deflated 74%)
  adding: META-INF/debug/fox_build_vars.txt (deflated 46%)
  adding: META-INF/com/ (stored 0%)
  adding: META-INF/com/google/ (stored 0%)
  adding: META-INF/com/google/android/ (stored 0%)
  adding: META-INF/com/google/android/update-binary (deflated 72%)
  adding: META-INF/com/google/android/updater-script (stored 0%)
  adding: magiskboot (deflated 50%)
  adding: sdcard/ (stored 0%)
  adding: sdcard/Fox/ (stored 0%)
  adding: sdcard/Fox/fox.bashrc (deflated 48%)
  adding: sdcard/Fox/FoxFiles/ (stored 0%)
  adding: sdcard/Fox/FoxFiles/Magisk.zip (deflated 10%)
  adding: sdcard/Fox/FoxFiles/uninstall.zip (deflated 10%)
  adding: sdcard/Fox/FoxFiles/AromaFM/ (stored 0%)
  adding: sdcard/Fox/FoxFiles/AromaFM/AromaFM.zip (deflated 4%)
  adding: INSTALL.txt (deflated 36%)
enter new zip file comment (end with .):
- Running ZIP command: /fox-work/fox_16.0/vendor/recovery/signature/sign_zip.sh -z /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip
- Signing /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip ...
-- Creating md5 for /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip
- Finished:
---------------------------------
 -rw-r--r-- 1 nobody nogroup 80960370 Oct 17 04:29 /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip
---------------------------------


		 ▒█████   ██▀███   ▄▄▄       ███▄    █   ▄████ ▓█████   █████▒▒█████  ▒██   ██▒
		▒██▒  ██▒▓██ ▒ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██   ▒▒██▒  ██▒▒▒ █ █ ▒░
		▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒████ ░▒██░  ██▒░░  █   ░
		▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ░▓█▒  ░▒██   ██░ ░ █ █ ▒ 
		░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒░▒████▒░▒█░   ░ ████▓▒░▒██▒ ▒██▒
		░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░ ▒ ░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
		  ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░ ░       ░ ▒ ▒░ ░░   ░▒ ░
		░ ░ ░ ▒    ░░   ░   ░   ▒      ░   ░ ░ ░ ░   ░    ░    ░ ░   ░ ░ ░ ▒   ░    ░  
		    ░ ░     ░           ░  ░         ░       ░    ░  ░           ░ ░   ░    ░  


===================Finished building OrangeFox===================

Recovery image: /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.img
          MD5: /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.img.md5

Recovery zip: /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip
          MD5: /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip.md5

==================================================================

#### build completed successfully (01:19:49 (hh:mm:ss)) ####


## last 300 lines of the combined step log
[ 99% 24496/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/ps (priority: 6)
[ 99% 24497/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/pwd (priority: 6)
[ 99% 24498/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/readlink (priority: 6)
[ 99% 24499/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/readelf (priority: 6)
[ 99% 24500/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/realpath (priority: 6)
[ 99% 24501/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/renice (priority: 6)
[ 99% 24502/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/restorecon (priority: 6)
[ 99% 24503/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/rm (priority: 6)
[ 99% 24504/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/rmdir (priority: 6)
[ 99% 24505/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/rmmod (priority: 6)
[ 99% 24506/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/rtcwake (priority: 6)
[ 99% 24507/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/recovery (priority: 6)
[ 99% 24508/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sed (priority: 6)
[ 99% 24509/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/runcon (priority: 6)
[ 99% 24510/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sendevent (priority: 6)
[ 99% 24511/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/seq (priority: 6)
[ 99% 24512/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/setenforce (priority: 6)
[ 99% 24513/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/setfattr (priority: 6)
[ 99% 24514/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/setprop (priority: 6)
[ 99% 24515/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/setsid (priority: 6)
[ 99% 24516/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sh (priority: 6)
[ 99% 24517/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sha1sum (priority: 6)
[ 99% 24518/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sha224sum (priority: 6)
[ 99% 24519/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sha256sum (priority: 6)
[ 99% 24520/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sha384sum (priority: 6)
[ 99% 24521/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sha512sum (priority: 6)
[ 99% 24522/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sleep (priority: 6)
[ 99% 24523/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sort (priority: 6)
[ 99% 24524/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/split (priority: 6)
[ 99% 24525/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/snapuserd (priority: 6)
[ 99% 24526/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/start (priority: 6)
[ 99% 24527/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/stat (priority: 6)
[ 99% 24528/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/stop (priority: 6)
[ 99% 24529/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/strings (priority: 6)
[ 99% 24530/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/stty (priority: 6)
[ 99% 24531/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/swapoff (priority: 6)
[ 99% 24532/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sync (priority: 6)
[ 99% 24533/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/swapon (priority: 6)
[ 99% 24534/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/sysctl (priority: 6)
[ 99% 24535/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tac (priority: 6)
[ 99% 24536/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tail (priority: 6)
[ 99% 24537/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/taskset (priority: 6)
[ 99% 24538/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tar (priority: 6)
[ 99% 24539/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/test (priority: 6)
[ 99% 24540/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tee (priority: 6)
[ 99% 24541/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/time (priority: 6)
[ 99% 24542/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/top (priority: 6)
[ 99% 24543/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/timeout (priority: 6)
[ 99% 24544/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/touch (priority: 6)
[ 99% 24545/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tr (priority: 6)
[ 99% 24546/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/true (priority: 6)
[ 99% 24547/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/truncate (priority: 6)
[ 99% 24548/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uclampset (priority: 6)
[ 99% 24549/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/tty (priority: 6)
[ 99% 24550/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/umount (priority: 6)
[ 99% 24551/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/ulimit (priority: 6)
[ 99% 24552/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uniq (priority: 6)
[ 99% 24553/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uname (priority: 6)
[ 99% 24554/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/unix2dos (priority: 6)
[ 99% 24555/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/unlink (priority: 6)
[ 99% 24556/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uptime (priority: 6)
[ 99% 24557/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/unshare (priority: 6)
[ 99% 24558/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/usleep (priority: 6)
[ 99% 24559/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uudecode (priority: 6)
[ 99% 24560/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uuencode (priority: 6)
[ 99% 24561/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/uuidgen (priority: 6)
[ 99% 24562/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/vi (priority: 6)
[ 99% 24563/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/vmstat (priority: 6)
[ 99% 24564/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/watch (priority: 6)
[ 99% 24565/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/watchdogd (priority: 6)
[ 99% 24566/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/which (priority: 6)
[ 99% 24567/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/wc (priority: 6)
[ 99% 24568/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/whoami (priority: 6)
[ 99% 24569/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/xargs (priority: 6)
[ 99% 24570/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/xxd (priority: 6)
[ 99% 24571/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/yes (priority: 6)
[ 99% 24572/24624] Symlink: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/bin/zcat (priority: 6)
[ 99% 24573/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/cgroups.json (priority: 6)
[ 99% 24574/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system/etc/ld.config.txt (priority: 6)
[ 99% 24575/24624] Install: /fox-work/out/host/linux-x86/lib/libc++.so (priority: 6)
[ 99% 24576/24624] host Prebuilt: fec_32 (/fox-work/out/host/linux-x86/obj32/EXECUTABLES/fec_intermediates/fec32) (priority: 6)
[ 99% 24577/24624] host Prebuilt: fec (/fox-work/out/host/linux-x86/obj/EXECUTABLES/fec_intermediates/fec) (priority: 6)
[ 99% 24578/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/plat_file_contexts (priority: 6)
[ 99% 24579/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/plat_service_contexts (priority: 6)
[ 99% 24580/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/plat_property_contexts (priority: 6)
[ 99% 24581/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system_ext_file_contexts (priority: 6)
[ 99% 24582/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system_ext_service_contexts (priority: 6)
[ 99% 24583/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/system_ext_property_contexts (priority: 6)
[ 99% 24584/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/vendor_file_contexts (priority: 6)
[ 99% 24585/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/vendor_service_contexts (priority: 6)
[ 99% 24586/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/vendor_property_contexts (priority: 6)
[ 99% 24587/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/odm_file_contexts (priority: 6)
[ 99% 24588/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/odm_property_contexts (priority: 6)
[ 99% 24589/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/product_file_contexts (priority: 6)
[ 99% 24590/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/product_service_contexts (priority: 6)
[ 99% 24591/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/product_property_contexts (priority: 6)
[ 99% 24592/24624] Install: /fox-work/out/target/product/OP5D2BL1/root/init.environ.rc (priority: 6)
[ 99% 24593/24624] Target recovery buildinfo: /fox-work/out/target/product/OP5D2BL1/recovery/root/prop.default (priority: 6)
[ 99% 24594/24624] //packages/modules/adb:adbd inject version symbol [linux_glibc] (priority: 6)
[ 99% 24595/24624] Install: /fox-work/out/host/linux-x86/bin/fec (priority: 5)
[ 99% 24596/24624] Install: /fox-work/out/host/linux-x86/bin/fec32 (priority: 5)
[ 99% 24597/24624] host Prebuilt: libadbd_auth (/fox-work/out/host/linux-x86/obj/SHARED_LIBRARIES/libadbd_auth_intermediates/libadbd_auth.so) (priority: 5)
[ 99% 24598/24624] host Prebuilt: libadbd_fs (/fox-work/out/host/linux-x86/obj/SHARED_LIBRARIES/libadbd_fs_intermediates/libadbd_fs.so) (priority: 5)
[ 99% 24599/24624] //external/avb:avbtool embedded python archive [linux_glibc] (priority: 6)
[ 99% 24600/24624] host Prebuilt: avbtool (/fox-work/out/host/linux-x86/obj/EXECUTABLES/avbtool_intermediates/avbtool) (priority: 5)
[ 99% 24601/24624] Install: /fox-work/out/host/linux-x86/bin/avbtool (priority: 4)
[ 99% 24602/24624] //system/tools/mkbootimg:mkbootimg Precompile the python sources of mkbootimg [linux_glibc] (priority: 6)
[ 99% 24603/24624] Install: /fox-work/out/host/linux-x86/lib64/libadbd_auth.so (priority: 4)
[ 99% 24604/24624] Install: /fox-work/out/host/linux-x86/lib64/libadbd_fs.so (priority: 4)
[ 99% 24605/24624] //packages/modules/adb:adbd strip adbd [linux_glibc] (priority: 5)
[ 99% 24606/24624] host Prebuilt: adbd (/fox-work/out/host/linux-x86/obj/EXECUTABLES/adbd_intermediates/adbd) (priority: 4)
[ 99% 24607/24624] //system/tools/mkbootimg:mkbootimg embedded python archive [linux_glibc] (priority: 5)
[ 99% 24608/24624] Install: /fox-work/out/host/linux-x86/bin/adbd (priority: 3)
[ 99% 24609/24624] host Prebuilt: mkbootimg (/fox-work/out/host/linux-x86/obj/EXECUTABLES/mkbootimg_intermediates/mkbootimg) (priority: 4)
[ 99% 24610/24624] Install: /fox-work/out/host/linux-x86/bin/mkbootimg (priority: 3)
[ 99% 24611/24624] Target ramdisk: /fox-work/out/target/product/OP5D2BL1/ramdisk.img (priority: 6)
[ 99% 24612/24624] //system/sepolicy:sepolicy.recovery Compiling cil files for sepolicy.recovery (priority: 8)
[ 99% 24613/24624] target Prebuilt: sepolicy.recovery (/fox-work/out/target/product/OP5D2BL1/obj/ETC/sepolicy.recovery_intermediates/sepolicy.recovery) (priority: 7)
[ 99% 24614/24624] Install: /fox-work/out/target/product/OP5D2BL1/recovery/root/sepolicy (priority: 6)
[ 99% 24615/24624] build /fox-work/out/target/product/OP5D2BL1/obj/PACKAGING/recovery_intermediates/ramdisk_files-timestamp (priority: 5)
#########################################################################
Variables exported from build/core/Makefile:
FOX_VENDOR_CMD=Fox_Before_Recovery_Image FOX_MANIFEST_VER=16.0 BOARD_BOOT_HEADER_VERSION=4 TARGET_ARCH=arm64 TARGET_RECOVERY_ROOT_OUT=/fox-work/out/target/product/OP5D2BL1/recovery/root TARGET_VENDOR_RAMDISK_OUT=/fox-work/out/target/product/OP5D2BL1/vendor_ramdisk MKBOOTIMG=/fox-work/out/host/linux-x86/bin/mkbootimg MKBOOTFS=/fox-work/out/host/linux-x86/bin/mkbootfs INTERNAL_RECOVERYIMAGE_ARGS="--ramdisk /fox-work/out/target/product/OP5D2BL1/ramdisk-recovery.img  --pagesize 4096" INTERNAL_MKBOOTIMG_VERSION_ARGS=--os_version 99.87.36 --os_patch_level 2099-12-31 BOARD_MKBOOTIMG_ARGS="--header_version 4 --pagesize 4096" TARGET_OUT=/fox-work/out/target/product/OP5D2BL1/system COMPRESSION_COMMAND=/fox-work/out/host/linux-x86/bin/lz4 -l -12 --favor-decSpeed INSTALLED_RECOVERYIMAGE_TARGET=/fox-work/out/target/product/OP5D2BL1/recovery.img BOARD_BOOTIMAGE_PARTITION_SIZE= BOARD_RECOVERYIMAGE_PARTITION_SIZE=0x6400000 BOARD_USES_RECOVERY_AS_BOOT= INTERNAL_KERNEL_CMDLINE= BOARD_INCLUDE_RECOVERY_RAMDISK_IN_VENDOR_BOOT= BOARD_MOVE_RECOVERY_RESOURCES_TO_VENDOR_BOOT= ORANGEFOX_CALLING_CARD=2.0 recovery_ramdisk=/fox-work/out/target/product/OP5D2BL1/ramdisk-recovery.img
#########################################################################
-- The device is a virtual A/B device  - disabling the init.d addon .... 
Building OrangeFox...
-- Setting up environment variables
-- ARM64 arch detected. Copying ARM64 binaries
-- Symlinking "resetprop" ...
-- This build will use magiskboot for patching boot images ...
-- Backing up /fox-work/out/target/product/OP5D2BL1/recovery/root//sbin/magiskboot to: /tmp/fox_build_tmp/ ...
-- Copying bash ...
-- Replacing the "sh" applet with bash ...
-- Cleaning up any ash stragglers...
-- Copying nano editor ...
-- Copying the GNU "tar" binary (gnutar) ...
-- Copying the GNU "sed" binary (gnused) ...
-- Copying the OrangeFox InfoZip "zip" binary ...
-- Enabling the App Manager ...
-- Detected Magisk version: 30.7
-- Generating the build ID 
-- Saving some original file sizes 
-- Building the recovery image, using the official AOSP recovery image builder ...
[ 99% 24616/24624] ----- Making uncompressed recovery ramdisk ------ (priority: 4)
[ 99% 24617/24624] //packages/modules/adb:adbd link adbd [apex31] (priority: 7)
[ 99% 24618/24624] Copy symbols with mapping: /fox-work/out/target/product/OP5D2BL1/symbols/apex/com.android.adbd/bin/adbd (priority: 6)
[ 99% 24619/24624] //packages/modules/adb:adbd strip adbd [apex31] (priority: 6)
[ 99% 24620/24624] target Prebuilt: adbd.com.android.adbd (/fox-work/out/target/product/OP5D2BL1/obj/EXECUTABLES/adbd.com.android.adbd_intermediates/adbd) (priority: 5)
[ 99% 24621/24624] Install: /fox-work/out/target/product/OP5D2BL1/apex/com.android.adbd/bin/adbd (priority: 4)
[ 99% 24622/24624] ----- Making compressed recovery ramdisk ------ (priority: 3)
[ 99% 24623/24624] build /fox-work/out/target/product/OP5D2BL1/recovery.img (priority: 2)
[100% 24624/24624] build recoveryimage (priority: 1)
#########################################################################
Variables exported from build/core/Makefile:
FOX_VENDOR_CMD=Fox_After_Recovery_Image FOX_MANIFEST_VER=16.0 BOARD_BOOT_HEADER_VERSION=4 TARGET_ARCH=arm64 TARGET_RECOVERY_ROOT_OUT=/fox-work/out/target/product/OP5D2BL1/recovery/root TARGET_VENDOR_RAMDISK_OUT=/fox-work/out/target/product/OP5D2BL1/vendor_ramdisk MKBOOTIMG=/fox-work/out/host/linux-x86/bin/mkbootimg MKBOOTFS=/fox-work/out/host/linux-x86/bin/mkbootfs INTERNAL_RECOVERYIMAGE_ARGS="--ramdisk /fox-work/out/target/product/OP5D2BL1/ramdisk-recovery.img  --pagesize 4096" INTERNAL_MKBOOTIMG_VERSION_ARGS=--os_version 99.87.36 --os_patch_level 2099-12-31 BOARD_MKBOOTIMG_ARGS="--header_version 4 --pagesize 4096" TARGET_OUT=/fox-work/out/target/product/OP5D2BL1/system COMPRESSION_COMMAND=/fox-work/out/host/linux-x86/bin/lz4 -l -12 --favor-decSpeed INSTALLED_RECOVERYIMAGE_TARGET=/fox-work/out/target/product/OP5D2BL1/recovery.img INSTALLED_BOOTIMAGE_TARGET= BOARD_BOOTIMAGE_PARTITION_SIZE= BOARD_RECOVERYIMAGE_PARTITION_SIZE=0x6400000 BOARD_USES_RECOVERY_AS_BOOT= INTERNAL_KERNEL_CMDLINE= ORANGEFOX_CALLING_CARD=4.0 recovery_ramdisk=/fox-work/out/target/product/OP5D2BL1/ramdisk-recovery.img
#########################################################################
-- The device is a virtual A/B device  - disabling the init.d addon .... 
-- Setting up environment variables
-- This is a system-as-root build ...
-- Copying recovery: "/fox-work/out/target/product/OP5D2BL1/recovery.img" --> "/fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.img" 
-- Creating the OrangeFox zip installer ...
- Creating /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip for deployment ...
-- A/B device - copying magiskboot to zip installer ... 
-- Saving the vAB flag ... 
-- Deleting the initd addon ...
- Running ZIP command: zip --exclude=*.git* -r9 /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip .
  adding: recovery.img (deflated 45%)
  adding: META-INF/ (stored 0%)
  adding: META-INF/debug/ (stored 0%)
  adding: META-INF/debug/default.prop (deflated 74%)
  adding: META-INF/debug/fox_build_vars.txt (deflated 46%)
  adding: META-INF/com/ (stored 0%)
  adding: META-INF/com/google/ (stored 0%)
  adding: META-INF/com/google/android/ (stored 0%)
  adding: META-INF/com/google/android/update-binary (deflated 72%)
  adding: META-INF/com/google/android/updater-script (stored 0%)
  adding: magiskboot (deflated 50%)
  adding: sdcard/ (stored 0%)
  adding: sdcard/Fox/ (stored 0%)
  adding: sdcard/Fox/fox.bashrc (deflated 48%)
  adding: sdcard/Fox/FoxFiles/ (stored 0%)
  adding: sdcard/Fox/FoxFiles/Magisk.zip (deflated 10%)
  adding: sdcard/Fox/FoxFiles/uninstall.zip (deflated 10%)
  adding: sdcard/Fox/FoxFiles/AromaFM/ (stored 0%)
  adding: sdcard/Fox/FoxFiles/AromaFM/AromaFM.zip (deflated 4%)
  adding: INSTALL.txt (deflated 36%)
enter new zip file comment (end with .):
- Running ZIP command: /fox-work/fox_16.0/vendor/recovery/signature/sign_zip.sh -z /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip
- Signing /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip ...
-- Creating md5 for /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip
- Finished:
---------------------------------
 -rw-r--r-- 1 nobody nogroup 80960370 Oct 17 04:29 /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip
---------------------------------


		 ▒█████   ██▀███   ▄▄▄       ███▄    █   ▄████ ▓█████   █████▒▒█████  ▒██   ██▒
		▒██▒  ██▒▓██ ▒ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██   ▒▒██▒  ██▒▒▒ █ █ ▒░
		▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▒████ ░▒██░  ██▒░░  █   ░
		▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ░▓█▒  ░▒██   ██░ ░ █ █ ▒ 
		░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒░▒████▒░▒█░   ░ ████▓▒░▒██▒ ▒██▒
		░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░ ▒ ░   ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░
		  ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░  ░ ░  ░ ░       ░ ▒ ▒░ ░░   ░▒ ░
		░ ░ ░ ▒    ░░   ░   ░   ▒      ░   ░ ░ ░ ░   ░    ░    ░ ░   ░ ░ ░ ▒   ░    ░  
		    ░ ░     ░           ░  ░         ░       ░    ░  ░           ░ ░   ░    ░  


===================Finished building OrangeFox===================

Recovery image: /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.img
          MD5: /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.img.md5

Recovery zip: /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip
          MD5: /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.zip.md5

==================================================================

#### build completed successfully (01:19:49 (hh:mm:ss)) ####

total 467184
drwxr-xr-x  2 runner runner      4096 Oct 17 04:28 FOX_AIK
-rw-r--r--  1 runner runner 104857600 Oct 17 04:28 OrangeFox-R12.0-Alpha-OP5D2BL1.img
-rw-r--r--  1 runner runner       107 Oct 17 04:28 OrangeFox-R12.0-Alpha-OP5D2BL1.img.md5
-rw-r--r--  1 runner runner  80960370 Oct 17 04:29 OrangeFox-R12.0-Alpha-OP5D2BL1.zip
-rw-r--r--  1 runner runner       107 Oct 17 04:29 OrangeFox-R12.0-Alpha-OP5D2BL1.zip.md5
-rw-r--r--  1 runner runner   1686576 Oct 17 03:26 all_modules.txt
-rw-r--r--  1 runner runner         1 Oct 17 04:23 android-info.txt
drwxr-xr-x  3 runner runner      4096 Oct 17 04:28 apex
-rw-r--r--  1 runner runner        84 Oct 17 03:09 build_fingerprint.txt
-rw-r--r--  1 runner runner        53 Oct 17 03:25 build_thumbprint.txt
-rw-r--r--  1 runner runner    156951 Oct 17 03:25 clean_steps.mk
drwxr-xr-x  2 runner runner      4096 Oct 17 04:23 debug_ramdisk
drwxr-xr-x  2 runner runner      4096 Oct 17 04:27 fake_packages
-rw-r--r--  1 runner runner       143 Oct 17 04:28 installed-files-ramdisk.json
-rw-r--r--  1 runner runner        28 Oct 17 04:28 installed-files-ramdisk.txt
drwxr-xr-x  9 runner runner      4096 Oct 17 04:22 obj
drwxr-xr-x  3 runner runner      4096 Oct 17 04:27 odm
-rw-r--r--  1 runner runner        43 Oct 17 03:26 previous_build_config.mk
-rw-r--r--  1 runner runner         0 Oct 17 03:26 previous_use_partial_compile.txt
drwxr-xr-x  3 runner runner      4096 Oct 17 04:27 product
drwxr-xr-x  9 runner runner      4096 Oct 17 04:28 ramdisk
-rw-r--r--  1 runner runner 186861056 Oct 17 04:28 ramdisk-recovery.cpio
-rw-r--r--  1 runner runner  68876441 Oct 17 04:28 ramdisk-recovery.img
-rw-r--r--  1 runner runner   1962690 Oct 17 04:28 ramdisk.img
drwxr-xr-x  3 runner runner      4096 Oct 17 03:10 recovery
-rw-r--r--  1 runner runner 104857600 Oct 17 04:28 recovery.img
drwxr-xr-x 27 runner runner      4096 Oct 17 04:28 root
drwxr-xr-x  9 runner runner      4096 Oct 17 04:29 symbols
drwxr-xr-x  6 runner runner      4096 Oct 17 04:28 system
== image: /fox-work/out/target/product/OP5D2BL1/OrangeFox-R12.0-Alpha-OP5D2BL1.img
   size: 104,857,600 bytes
   header v4, header_size 1584, kernel 0, ramdisk 68,876,441
   cmdline: ''
   lz4 legacy: 23 blocks -> 186,861,056 bytes cpio
   avb hash footer: AVB0 at 68,882,432 (832 B)
== ramdisk: 5,012 entries (4,787 files, 225 symlinks)
   kernel modules: 483
   vibration related: 107
   modules.load.recovery: 456 entries, 0 missing
   device tree recovery/root: 829 files, 0 missing
   content check: 829 compared, 0 differ
   ok   system/bin/recovery
   ok   system/bin/twrp
   ok   system/etc/twrp.flags
   ok   vendor/bin/hw/vendor.oplus.hardware.vibrator-service
   ok   vendor/etc/init/vibrator-default.rc
   ok   odm/etc/vibrator/vibrator_effect.json

== all checks passed
::notice::image self-check exit=0
### ldcheck vendor/bin/qseecomd
readelf: Warning: Separate debug info file /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libc.so found, but CRC does not match - ignoring
libs: ['vendor/bin/qseecomd', 'system/lib64/libcutils.so', 'system/lib64/libutils.so', 'system/lib64/liblog.so', 'vendor/lib64/libQSEEComAPI.so', 'vendor/lib64/libdrmfs.so', 'vendor/lib64/libminkdescriptor.so', 'vendor/lib64/libdmabufheap.so', 'system/lib64/libc++.so', 'system/lib64/libc.so', 'system/lib64/libm.so', 'system/lib64/libdl.so', 'system/lib64/libbase.so', 'system/lib64/libvndksupport.so', 'vendor/lib64/libqcbor.so', 'vendor/lib64/libdiag.so', 'system/lib64/libxml2.so', 'system/lib64/ld-android.so', 'system/lib64/libdl_android.so', 'system/lib64/libandroidicu.so', 'system/lib64/libicuuc.so', 'system/lib64/libicui18n.so']
unused: {'vendor/lib64/libQSEEComAPI.so', 'vendor/lib64/libdrmfs.so', 'system/lib64/libicuuc.so', 'system/lib64/libicui18n.so', 'system/lib64/libxml2.so', 'system/lib64/libdl_android.so', 'vendor/lib64/libdiag.so', 'system/lib64/libvndksupport.so', 'system/lib64/libm.so', 'system/lib64/libandroidicu.so', 'system/lib64/libutils.so'}
### ldcheck vendor/bin/hw/vendor.oplus.hardware.vibrator-service
readelf: Warning: Separate debug info file /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libc.so found, but CRC does not match - ignoring
libs: ['vendor/bin/hw/vendor.oplus.hardware.vibrator-service', 'system/lib64/android.hardware.vibrator-V2-ndk.so', 'vendor/lib64/vendor.aac.hardware.richtap.vibrator-V2-ndk.so', 'vendor/lib64/vendor.oplus.hardware.vibrator-V1-ndk.so', 'vendor/lib64/vendor.oplus.hardware.oplusvibrator-V2-ndk.so', 'vendor/lib64/libsoc_helper.so', 'system/lib64/libcutils.so', 'system/lib64/libutils.so', 'system/lib64/libbase.so', 'vendor/lib64/liboplusvibratoreffect.so', 'system/lib64/libbinder_ndk.so', 'vendor/lib64/libaacvibrator.so', 'vendor/lib64/libsivibrator.so', 'vendor/lib64/libtfavib.so', 'system/lib64/liblog.so', 'system/lib64/libc++.so', 'system/lib64/libc.so', 'system/lib64/libm.so', 'system/lib64/libdl.so', 'system/lib64/libvndksupport.so', 'system/lib64/libjsoncpp.so', 'system/lib64/libbinder.so', 'system/lib64/ld-android.so', 'system/lib64/libdl_android.so', 'system/lib64/libapexsupport.so']
unused: {'vendor/lib64/vendor.oplus.hardware.vibrator-V1-ndk.so', 'system/lib64/libbase.so'}
### ldcheck vendor/bin/hw/android.hardware.security.keymint-service-qti
readelf: Warning: Separate debug info file /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libc.so found, but CRC does not match - ignoring
libs: ['vendor/bin/hw/android.hardware.security.keymint-service-qti', 'system/lib64/liblog.so', 'system/lib64/libcutils.so', 'system/lib64/libbase.so', 'system/lib64/libutils.so', 'system/lib64/libhardware.so', 'system/lib64/libbinder_ndk.so', 'system/lib64/libhidlbase.so', 'system/lib64/android.hardware.keymaster@4.0.so', 'vendor/lib64/libqtikeymint.so', 'system/lib64/libcrypto.so', 'system/lib64/android.hardware.security.keymint-V3-ndk.so', 'system/lib64/android.hardware.security.rkp-V3-ndk.so', 'system/lib64/android.hardware.security.secureclock-V1-ndk.so', 'system/lib64/android.hardware.security.sharedsecret-V1-ndk.so', 'system/lib64/libc++.so', 'system/lib64/libc.so', 'system/lib64/libm.so', 'system/lib64/libdl.so', 'system/lib64/libvndksupport.so', 'system/lib64/libbinder.so', 'system/lib64/android.hardware.keymaster@3.0.so', 'vendor/lib64/libkeymasterdeviceutils.so', 'vendor/lib64/libqcbor.so', 'system/lib64/libkeymaster_messages.so', 'system/lib64/android.hardware.keymaster@4.1.so', 'vendor/lib64/libkeymasterutils.so', 'system/lib64/ld-android.so', 'system/lib64/libdl_android.so', 'system/lib64/libapexsupport.so', 'vendor/lib64/libion.so', 'vendor/lib64/libdmabufheap.so', 'vendor/lib64/libminkdescriptor.so', 'vendor/lib64/libQSEEComAPI.so']
unused: {'system/lib64/libbase.so', 'system/lib64/libm.so', 'system/lib64/libhidlbase.so', 'system/lib64/android.hardware.keymaster@4.0.so', 'system/lib64/android.hardware.keymaster@3.0.so', 'system/lib64/android.hardware.keymaster@4.1.so', 'vendor/lib64/libion.so', 'system/lib64/libhardware.so'}
### ldcheck vendor/bin/hw/android.hardware.weaver-service.nxp
readelf: Warning: Separate debug info file /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libc.so found, but CRC does not match - ignoring
libs: ['vendor/bin/hw/android.hardware.weaver-service.nxp', 'system/lib64/android.hardware.weaver-V2-ndk.so', 'system/lib64/libbase.so', 'system/lib64/libbinder_ndk.so', 'system/lib64/liblog.so', 'vendor/lib64/ese_weaver.so', 'vendor/lib64/vendor.oplus.hardware.weaver-V1-ndk.so', 'system/lib64/libc++.so', 'system/lib64/libc.so', 'system/lib64/libm.so', 'system/lib64/libdl.so', 'system/lib64/libbinder.so', 'system/lib64/libutils.so', 'vendor/lib64/android.se.omapi-V1-ndk.so', 'system/lib64/libcutils.so', 'vendor/lib64/libjc_keymint_transport_nxp.so', 'system/lib64/libhardware.so', 'system/lib64/libhidlbase.so', 'system/lib64/ld-android.so', 'system/lib64/libapexsupport.so', 'system/lib64/libvndksupport.so', 'vendor/lib64/android.hardware.secure_element@1.0.so', 'vendor/lib64/android.hardware.secure_element@1.1.so', 'vendor/lib64/android.hardware.secure_element@1.2.so', 'system/lib64/libdl_android.so']
unused: {'system/lib64/libm.so', 'system/lib64/libbase.so', 'system/lib64/libhardware.so'}
### ldcheck vendor/bin/hw/android.hardware.secure_element-service.qti
readelf: Warning: Separate debug info file /fox-work/out/target/product/OP5D2BL1/recovery/root/system/lib64/libc.so found, but CRC does not match - ignoring
libs: ['vendor/bin/hw/android.hardware.secure_element-service.qti', 'vendor/lib64/libQSEEComAPI.so', 'vendor/lib64/hw/libEseUtils.so', 'vendor/lib64/libGPQeSE.so', 'system/lib64/libbase.so', 'system/lib64/liblog.so', 'system/lib64/libutils.so', 'system/lib64/libbinder_ndk.so', 'vendor/lib64/android.hardware.secure_element-V1-ndk.so', 'system/lib64/libc++.so', 'system/lib64/libc.so', 'system/lib64/libm.so', 'system/lib64/libdl.so', 'vendor/lib64/libdmabufheap.so', 'vendor/lib64/libqcbor.so', 'vendor/lib64/libminkdescriptor.so', 'system/lib64/libhidlbase.so', 'system/lib64/libhardware.so', 'system/lib64/libcutils.so', 'vendor/lib64/android.hardware.secure_element@1.0.so', 'vendor/lib64/libGPTEE_vendor.so', 'system/lib64/libvndksupport.so', 'system/lib64/libbinder.so', 'system/lib64/ld-android.so', 'system/lib64/libdl_android.so', 'system/lib64/libapexsupport.so']
unused: {'vendor/lib64/android.hardware.secure_element@1.0.so', 'system/lib64/libhardware.so', 'system/lib64/libm.so', 'system/lib64/libhidlbase.so'}
/dev/root       146G  127G   19G  88% /
92618162996e116a78af53ad675d18543b4fa94fd43e8246b869df974df5ece2  recovery.img
049017576546744aa1973712cbc4b9e7  recovery.img
total 213612
-rw-r--r-- 1 runner runner 104857600 Oct 17 04:29 OrangeFox-R12.0-Alpha-OP5D2BL1.img
-rw-r--r-- 1 runner runner       107 Oct 17 04:29 OrangeFox-R12.0-Alpha-OP5D2BL1.img.md5
-rw-r--r-- 1 runner runner  80960370 Oct 17 04:29 OrangeFox-R12.0-Alpha-OP5D2BL1.zip
-rw-r--r-- 1 runner runner       107 Oct 17 04:29 OrangeFox-R12.0-Alpha-OP5D2BL1.zip.md5
-rw-r--r-- 1 runner runner  68876441 Oct 17 04:29 ramdisk-recovery.img
release tag: fox16-12471a2217c0
