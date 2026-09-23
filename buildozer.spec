
[app]
title = XSMB Pro 365
package.name = xsmbpro365
package.domain = com.xsmbpro.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1
requirements = python3,kivy==2.3.0
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
