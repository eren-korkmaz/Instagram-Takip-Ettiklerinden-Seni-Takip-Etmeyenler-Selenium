from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class InstaBot:
    def __init__(self, un, pw):
        self.driver = webdriver.Chrome()
        self.un = un
        self.driver.get("https://instagram.com")
        sleep(2)
        # sleep(2)

        login_un = self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(un)
        sleep(2)
        login_pw = self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(pw)
        sleep(2)
        # self.driver.find_element_by_xpath().click()
        self.bisiyetikla("//button[@type=\"submit\"]")

        input("Login Oldu Enterla")

        # notnow click
        # self.driver.find_element_by_xpath().click()
        self.bisiyetikla("//button[contains(text(), 'Şimdi Değil')]")

    def eleman_varmi(self, eleman):

        try:
            elements = self.driver.find_element_by_xpath(eleman)
            return elements
        except NoSuchElementException:
            return None

    def bisiyetikla(self, neye):
        if self.eleman_varmi(neye):
            if neye == "elle":  # elle yapıyorum sen devam et
                pass
            else:
                self.driver.find_element_by_xpath(neye).click()
        else:
            yenieleman = input("eleman bulunamadı yeni bir değer girin : ")
            self.bisiyetikla(yenieleman)

    def lightbox_kapa(self):
        kpt = "0"
        #tiklanacek = "//div[contains(concat(' ', normalize-space(@class), ' '), ' WaOAr ')]"
        tiklanacek = "/html/body/div[4]/div/div[1]/div/div[2]/button"
        while kpt != "2":
            self.bisiyetikla(tiklanacek)
            kpt = input("light box kapatıldımı")
            if kpt == "0":
                tiklanacek = input("yeni degeri girin : ")
            elif kpt == "1":
                print("tekrar deneniyor")
            elif kpt == "2":
                tiklanacek = input("yeni degeri girin")

    def getir_takip_etmeyenler(self):

        # profile gir
        # self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.un)).click()
        self.bisiyetikla("//a[contains(@href,'/{}')]".format(self.un))
        input("Profil Sayfası Açıldı")

        # takipçiye tıklar
        # self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        self.bisiyetikla("//a[contains(@href,'/following')]")
        input("Takip Ettiklerim Açıldı Enterla")

        following = self._get_names()
        print(following)

        input("Takip Ettiklerim Listesi Alındı Enterla")

        # self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        self.bisiyetikla("//a[contains(@href,'/followers')]")
        input("Takipçilerim Açıldı Enterla")

        followers = self._get_names()
        print(followers)

        input("Takipçilerim Alındı Enterla")

        not_following_back = [user for user in following if user not in followers]

        print("*************Senin Takip Ettiklerin Ama Seni Takip Etmeyenler***********")
        print(not_following_back)

    def _get_names(self):

        scroll_box = self.driver.find_element_by_xpath(
            "//div[contains(concat(' ', normalize-space(@class), ' '), ' isgrP ')]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        input(" * Lightbox kapatılacak")
        self.lightbox_kapa()

        return names


ReklamBot = InstaBot("kullanici_adi", "sifre")
ReklamBot.getir_takip_etmeyenler()
