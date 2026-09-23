[app]
title = XSMB Pro 365
package.name = xsmbpro365
package.domain = com.xsmbpro.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.1.1,requests,certifi,charset-normalizer,urllib3
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0

[app:permissions]
android.permissions = INTERNET

[buildozer:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = android
android.accept_sdk_license_agreement = True
android.ant = auto
android.archs = arm64-v8a, armeabi-v7a
