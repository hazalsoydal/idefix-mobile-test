from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):

    # hint/text yok, direkt class ile buluyoruz
    EMAIL_INPUT    = (AppiumBy.XPATH, '//android.widget.EditText')
    DEVAM_ET_BTN   = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Devam Et"]')
    PASSWORD_INPUT = (AppiumBy.XPATH, '//android.widget.EditText')
    GIRIS_YAP_BTN  = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Giriş Yap"]')

    def enter_email(self, email):
        print(f"mail adresi giriliyor: {email}")
        self.type_text(*self.EMAIL_INPUT, email)

    def click_devam_et(self):
        print("devam et butonuna basılıyor")
        self.click(*self.DEVAM_ET_BTN)

    def enter_password(self, password):
        print("şifre giriliyor")
        self.type_text(*self.PASSWORD_INPUT, password)

    def click_giris_yap(self):
        print("giriş yap butonuna basılıyor")
        self.click(*self.GIRIS_YAP_BTN)

    def login(self, email, password):
        self.enter_email(email)
        self.click_devam_et()
        self.enter_password(password)
        self.click_giris_yap()