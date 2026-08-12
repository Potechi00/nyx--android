[app]
title = NYX
package.name = nyxassistant
package.domain = com.nyx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 🟢 DIPERBAIKI: Menambahkan 'pillow' untuk mendukung gambar .jpg
requirements = python3,kivy==2.3.0,plyer,pillow

orientation = portrait
android.permissions = RECORD_AUDIO,INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = sdl2

p4a.branch = v2024.01.21

[buildozer]
log_level = 2
warn_on_root = 1
