[app]
title = XSMB Pro 365
package.name = xsmbpro365
package.domain = com.xsmb.app
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2

[app:permissions]
android.permissions = INTERNET

[android]
api = 33
minapi = 21
accept_sdk_license_agreements = True
