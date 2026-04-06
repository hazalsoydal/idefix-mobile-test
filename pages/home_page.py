import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class HomePage(BasePage):

    ALLOW_NOTIFICATION_BTN = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
    HESABIM_TAB  = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Hesabım, Tab 5 of 5"]')
    ANASAYFA_TAB = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Anasayfa, Tab 1 of 5"]')
    POPUP_CLOSE  = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Kapat"]')

    def allow_notifications(self):
        if self.is_element_present(*self.ALLOW_NOTIFICATION_BTN, timeout=0.5):
            print("popupta allow'a bas")
            self.click(*self.ALLOW_NOTIFICATION_BTN)
        else:
            print("popup cıkmadı devam et")

    def go_to_hesabim(self):
        print("hesabıma basılıyor")
        if self.is_element_present(*self.HESABIM_TAB, timeout=0.5):
            self.click(*self.HESABIM_TAB)
        else:
            print("xpath bulamadığım için xpath ile tıkliyorum")
            self.driver.tap([(972, 2253)])

    def close_popup(self):
        if self.is_element_present(*self.POPUP_CLOSE, timeout=0.5):
            print("popup kapatılıyor")
            self.click(*self.POPUP_CLOSE)
        else:
            print("popup yok devam et")

    def go_to_anasayfa(self):
        print("anasayfaya gidiliyor")
        self.driver.tap([(108, 2253)])