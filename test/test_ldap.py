from selenium import webdriver
import unittest
import time



class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_login(self):
        wd = self.wd
        self.open_dozor(wd)
        self.login(wd)
        wd.get("https://10.201.64.31/#!dashboard")
        wd.find_element_by_id("main-menu-1041-innerCt").click()
        wd.find_element_by_id("button-1055-btnInnerEl").click()
        wd.find_element_by_xpath("//div[@id='configuration-groups-dataview-3542']/div[4]/div[4]/div/div").click()

    def login(self, wd):
        wd.find_element_by_id("textfield-1013-inputEl").click()
        wd.find_element_by_id("textfield-1013-inputEl").clear()
        wd.find_element_by_id("textfield-1013-inputEl").send_keys("superadmin")
        wd.find_element_by_id("textfield-1017-inputEl").click()
        wd.find_element_by_id("textfield-1017-inputEl").clear()
        wd.find_element_by_id("textfield-1017-inputEl").send_keys("Zaq1@wsX")
        time.sleep(1)
        wd.find_element_by_xpath(u"//*/text()[normalize-space(.)='Login']/parent::*").click()
        time.sleep(3)

    def open_dozor(self, wd):
        wd.get("https://10.201.64.31/#dashboard")
        time.sleep(5)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()