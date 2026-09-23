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
