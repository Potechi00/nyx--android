[app]
title = NYX
package.name = nyxassistant
package.domain = com.nyx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 🟢 Kunci versi untuk stabilitas jangka panjang
requirements = python3==3.11.9,kivy==2.3.0,plyer

orientation = portrait
android.permissions = RECORD_AUDIO,INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
