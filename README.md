# Idefix Mobile Automation — POM Structure

# 1. Install Appium globally
npm install -g appium

# 2. Install UiAutomator2 driver
Appium driver install uiautomator2

# 3. Install Python dependencies
pip install Appium-Python-Client pytest


## Project Structure

```
idefix_automation/
├── capabilities.py        ← Appium desired capabilities
├── pages/
│   ├── base_page.py       ← Shared helpers (wait, click, type)
│   ├── home_page.py       ← Notification popup + bottom menu
│   └── login_page.py      ← Email, Devam Et, Password, Giriş Yap
└── tests/
    └── test_login.py      ← Full E2E test
```

## How to Run

```bash
# Terminal 1 — Start Appium server
appium

# Terminal 2 — Start your emulator in Android Studio, then run:
cd idefix_automation
pytest tests/test_login.py -v -s
```

## Important: Fix the Locators with Appium Inspector


### How to use Appium Inspector

1. Download from: https://github.com/appium/appium-inspector/releases
2. Start Appium server (`appium`)
3. Open Appium Inspector → enter these capabilities:
   ```json
   {
     "platformName": "Android",
     "appium:deviceName": "Pixel 7",
     "appium:platformVersion": "14.0",
     "appium:appPackage": "com.idefix.android",
     "appium:appActivity": ".MainActivity",
     "appium:automationName": "UiAutomator2"
   }
   ```
4. Click **Start Session**
5. Click elements in the screenshot to see their `resource-id`, `text`, `content-desc`
6. Update the locators in `home_page.py` and `login_page.py`

### How to find appPackage & appActivity

With your emulator running and the app open:
```bash
adb shell dumpsys window | grep -E "mCurrentFocus|mFocusedApp"
```

## Locators to verify

| File | Locator constant | What to look for in Inspector |
|------|-----------------|-------------------------------|
| `home_page.py` | `HESABIM_TAB` | `resource-id` of the Hesabım tab |
| `login_page.py` | `EMAIL_INPUT` | `resource-id` of the email EditText |
| `login_page.py` | `DEVAM_ET_BTN` | `resource-id` or `text` of Devam Et |
| `login_page.py` | `PASSWORD_INPUT` | `resource-id` of the password EditText |
| `login_page.py` | `GIRIS_YAP_BTN` | `resource-id` or `text` of Giriş Yap |
