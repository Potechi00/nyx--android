[app]

title = NYX
package.name = nyxassistant
package.domain = com.nyx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,plyer
orientation = portrait

android.permissions = RECORD_AUDIO,INTERNET

android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

android.arch = arm64-v8a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
