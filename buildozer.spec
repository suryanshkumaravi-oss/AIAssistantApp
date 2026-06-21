[app]
title = Srijal AI
package.name = srijalai
package.domain = com.srijal.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy==2.1.0
orientation = portrait
fullscreen = 0
author = Suryansh

android.api = 31
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.permissions = INTERNET
android.archs = arm64-v8a
android.accept_sdk_license = True

p4a.branch = develop
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
