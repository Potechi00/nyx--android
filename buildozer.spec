[app]

title = NYX
package.name = nyxassistant
package.domain = com.nyx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 3.0
requirements = python3==3.14.2,kivy==2.3.0,kivymd==1.1.1,plyer,cython==3.1.0,sh<2.0
orientation = portrait

android.permissions = RECORD_AUDIO,INTERNET

android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

android.archs = arm64-v8a
android.allow_backup = True

p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
