[app]

title = NYX
package.name = nyxassistant
package.domain = com.nyx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 🟢 SUDAH DIPERBAIKI: Hapus cython & hostpython3 dari requirements runtime
requirements = python3,kivy==2.2.1,plyer

orientation = portrait

android.permissions = RECORD_AUDIO,INTERNET

android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

# 🟢 SUDAH DIPERBAIKI: Mendukung HP 64-bit dan 32-bit/emulator
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
