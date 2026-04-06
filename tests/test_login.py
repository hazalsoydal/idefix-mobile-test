import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # calisan dosyanin tam yolu

import pytest #test calistirmak icin kullanılan kutupahne
from appium import webdriver
from capabilities import options, APPIUM_SERVER_URL
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage

EMAIL    = "hazal.soydal@idefix.com"
PASSWORD = "idefixHazal680*"

# --- Kart Bilgileri ---
KART_NO   = "4111111111111111"  
KART_ISIM = "HAZAL HAZAL"     
KART_SKT  = "12/26"            
KART_CVV  = "123"              

@pytest.fixture(scope="function") #testten once hazırlık yapan testten sonra temizlik yapan bi fonksiyon. yield d'den once hazırlık.
#yield d'den sonra temizlik yapar. scope="function" dersek her testten once ve sonra calisir, scope="class" dersek sadece class basinda ve sonunda calisir

def driver():                                   #options yine capabilities.py den geliyor
    d = webdriver.Remote(APPIUM_SERVER_URL, options=options) #uzaktaki sunucuya bağlan demek.yani kendi pcmdeki appium sunucusu
    # Uygulamayı başlat
    d.activate_app("tr.com.idefix.android") #emulatordeki idefix uygulamasını baslatıyor
    yield d  #dur testi calıstır sonra buraya geri don 
    d.quit() #test bitti baglantıyı kapat demek oluyor
    #return kullansaydik d.quit calismicakti, baglanti acik kalıcaktı. ama yield sayesinde test bittikten sonra temizlik yapıldı.yield simdi dur sonra devam et demek giib bir sey

    
class TestIdefixLogin:   #bir sınıf tanımı, pytest bu sınıfı goruyor
    def test_login_and_search(self, driver):    #burda page objectler oluşturuluyor hepsine aynı driver veriliyor
        home_page   = HomePage(driver)
        login_page  = LoginPage(driver)
        search_page = SearchPage(driver)

        # bildirim popupına ok dedim 
        home_page.allow_notifications()

        # hesap giris fln
        home_page.go_to_hesabim()
        login_page.login(EMAIL, PASSWORD)

        # popup kapat
        home_page.close_popup()

        # anasayfa git
        home_page.go_to_anasayfa()

        # 5. Arama yap
        search_page.search("kulaklik")

        # 6. İlk ürünü sepete ekle
        search_page.add_first_product_to_cart()

        # 7. Sepete git
        search_page.go_to_cart()

        # 8. Sepeti onayla
        search_page.sepeti_onayla()

        # 9. Kart bilgilerini gir, formu onayla ve siparişi tamamla
        search_page.kart_bilgilerini_gir(KART_NO, KART_ISIM, KART_SKT, KART_CVV)

        search_page.sozlesme_onayla()


        print("oldu")