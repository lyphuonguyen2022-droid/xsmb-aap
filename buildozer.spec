[app]
title = XSMB Pro 365
package.name = xsmbpro365
package.domain = com.xsmbpro.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.1.1,requests
orientation = portrait

[buildozer]
log_level = 2

[app:permissions]
android.permissions = INTERNET

[buildozer:android]
android.api = 33
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
