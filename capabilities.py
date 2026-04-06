from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Pixel 7"
options.platform_version = "14.0"
options.app_package = "tr.com.idefix.android"
options.app_activity = ".MainActivity"
options.no_reset = True
options.auto_grant_permissions = False

APPIUM_SERVER_URL = "http://localhost:4723"