#gerekli kutuphaneleri import ediyoruz burda
from appium.webdriver.common.appiumby import AppiumBy #element bulmak ıcın
from selenium.webdriver.support.ui import WebDriverWait #element gorunene kadar bekle
from selenium.webdriver.support import expected_conditions as EC #bekleme kosulları
from selenium.common.exceptions import TimeoutException #zaman asimi hatasi icin kullanilir


#TUM SAYFA SINIFLARININ MIRAS ALINACAGI SINIF BASE PAGE DENiyo
class BasePage:

    DEFAULT_TIMEOUT = 10 #bir elementi bulmak icin max 10 saniye bekle demek
    
    def __init__(self, driver):
        self.driver = driver #self.driver sayesinde sınıfın tüm metodları bu driver'a erişebilir:
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)
        #self.driver → nesneye ait, her yerden erişilir driver → sadece __init__ içinde var, dışarıdan erişilemez

  
#webdriverwait su kadar sanşyeboyunca dene demek. t saniye boyunca asagidaki kosul gerceklesene kadar bekle dedik
    def wait_for_element(self, by, value, timeout=None):
        t = timeout or self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, t).until(
            EC.presence_of_element_located((by, value))
        )
    
#sadece gorunmesı yetmez, tıklanabilir olması gerekir
    def wait_for_element_clickable(self, by, value, timeout=None):
        t = timeout or self.DEFAULT_TIMEOUT
        return WebDriverWait(self.driver, t).until(
            EC.element_to_be_clickable((by, value))
        )

#burda elementin var mi yok mu bakıyo sadece gorunmesı yetmez tıklanablir olmalı
    def is_element_present(self, by, value, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False


    def click(self, by, value):
        element = self.wait_for_element_clickable(by, value)
        element.click()


#burda tıklayıp temizliyo sonra metni uazıo
    def type_text(self, by, value, text):
        element = self.wait_for_element_clickable(by, value)
        element.click()
        element.clear()
        element.send_keys(text)


    def get_text(self, by, value):
        element = self.wait_for_element(by, value)
        return element.text
