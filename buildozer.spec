[app]

# (str) Title of your application
title = NYX

# (str) Package name
package.name = nyx

# (str) Package domain (reverse DNS)
package.domain = com.potechioc

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (str) Android API level
android.api = 34

# (str) Android minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 23b

# (str) Android SDK version
android.sdk = 34

# (str) Android permissions
android.permissions = INTERNET, RECORD_AUDIO

# (bool) Enable/disable debug mode
android.debug = True

# (bool) Enable/disable logcat
android.logcat = True

[buildozer]

# (int) Log level (0-2)
log_level = 2

# (bool) Warnings
warn_on_root = 1