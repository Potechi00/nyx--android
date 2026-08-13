[app]

# (str) Title of your application
title = NYX

# (str) Package name
package.name = nyxapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.nyx

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) Application versioning
version = 3.0.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,requests,urllib3,certifi,chardet,idna

# (str) Supported orientation (portrait/landscape)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions (Izin Akses Aplikasi)
android.permissions = INTERNET,RECORD_AUDIO

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enables Android auto backup feature
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

# Timeout jaringan p4a
p4a.timeout = 60
