from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import time


class SearchPage(BasePage):

    SEPETE_EKLE  = (AppiumBy.XPATH, '(//android.widget.Button[@content-desc="Sepete Ekle"])[1]')
    SEPETE_GIT   = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Sepete Git"]')
    SEPETI_ONAYLA = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Sepeti Onayla"]')
    
    KREDI_KARTI_SEC = (AppiumBy.ACCESSIBILITY_ID, 'Kredi Kartı / Banka Kartı ile Öde')

    TEK_CEKIM = (AppiumBy.XPATH, '//android.view.View[contains(@content-desc, "Tek Çekim")]')

    KART_NUMARASI   = (AppiumBy.XPATH, '//android.view.View[@content-desc="Ödeme Yöntemi"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')


    KART_ISIM       = (AppiumBy.XPATH, '//android.view.View[@content-desc="Ödeme Yöntemi"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')


    SON_KULLANMA    = (AppiumBy.XPATH, '//android.view.View[@content-desc="Ödeme Yöntemi"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[3]')


    GUVENLIK_KODU   = (AppiumBy.XPATH, '//android.view.View[@content-desc="Ödeme Yöntemi"]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[4]')


    ONAY_CHECKBOX   = (AppiumBy.XPATH, '//android.widget.CheckBox')


    ONAYLA_VE_BITIR = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Onayla ve Bitir"]')

    def search(self, keyword):
        print(f"aranıyor: {keyword}")
        # 2 kez tıkla
        self.driver.tap([(485, 209)])
        time.sleep(1)
        self.driver.tap([(485, 209)])
        time.sleep(1)
        # Eğer input alanı varsa ve içinde yazı varsa temizle
        search_input = (AppiumBy.XPATH, '//android.widget.EditText')
        if self.is_element_present(*search_input, timeout=0.5):
            element = self.wait_for_element(*search_input)
            if element.text and element.text != "":
                print("mevcut yazı tanımlanıyor")
                element.clear()

        # aramayı yaz
        self.driver.execute_script("mobile: type", {"text": keyword})
        time.sleep(0.5)
        self.driver.press_keycode(66)  # Enter
        # Arama sonuçları yüklensin — ilk ürün görününce devam et
        self.wait_for_element(*self.SEPETE_EKLE)
        print("arama tamamlandı")
   
    def add_first_product_to_cart(self):
        print("ilk urunu ekliyorum")
        self.click(*self.SEPETE_EKLE)
        time.sleep(0.5)  # popup açılsın


    def go_to_cart(self):
        print("sepete gidiyorum")
        self.click(*self.SEPETE_GIT)

    def sepeti_onayla(self):
        print("sepet onyalanıyor")
        self.driver.tap([(847, 2046)])

    def kart_bilgilerini_gir(self, kart_no, isim, skt, cvv):
        print("ödeme sayfasına gidiliyor")

        # Kredi Kartı ile öde
        print("Kredi Kartı / Banka Kartı ile Öde seçiliyor...")
        self.click(*self.KREDI_KARTI_SEC)
        time.sleep(1)  

        # Kart numarasını yaz
        print(f"kart numarası giriliyor: {kart_no}")
        self.type_text(*self.KART_NUMARASI, kart_no)
        time.sleep(0.2)

        # Kart üzerindeki ismi yaz
        print(f"kart ismi giriliyor: {isim}")
        self.type_text(*self.KART_ISIM, isim)
        time.sleep(0.2)

        # Son kullanma tarihini yaz 
        print(f"son kullanma tarihi giriliyor: {skt}")
        self.type_text(*self.SON_KULLANMA, skt)
        time.sleep(0.2)

        # Güvenlik kodunu yaz
        print(f"güvenlik kodu giriliyor: {cvv}")
        self.type_text(*self.GUVENLIK_KODU, cvv)
        time.sleep(0.2)

        # Klavyeyi kapat
        self.driver.press_keycode(66)
        time.sleep(0.3)

        # Tek Çekim seçeneğine tıkla
        # Uygulama otomatik scroll eder ve checkbox ekrana gelir
        print("tek çekim seçiliyor...")
        self.click(*self.TEK_CEKIM)
        time.sleep(2)  # Uygulamanın scroll'unu tamamlaması için bekle

        self.driver.swipe(540, 1800, 540, 100, 800)
        time.sleep(0.5)
        self.driver.swipe(540, 1800, 540, 100, 800)
        time.sleep(0.5)
        

        # Checkbox görünene kadar bekle ve tıkla
        print("ön bilgilendirme checkbox'ı işaretleniyor...")
        self.wait_for_element_clickable(AppiumBy.XPATH, '//android.widget.CheckBox')
        self.click(*self.ONAY_CHECKBOX)
        time.sleep(0.5)

        # Onayla ve Bitir
        print("onayla ve bitir butonuna tıklanıyor...")
        self.click(*self.ONAYLA_VE_BITIR)
        time.sleep(2)
        print("ödeme tamamlandı!")