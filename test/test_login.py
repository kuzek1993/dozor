# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options

class AddContact(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\\Users\\v.kochergin\\AppData\\Local\\Mozilla Firefox\\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\\Users\\v.kochergin\\Downloads\\geckodriver.exe', options=options)
        self.wd.implicitly_wait(30)

    def test_connect_ldap(self):
        wd = self.wd
        self.open_dozor(wd)
        self.login(wd)
        self.close_redwindow(wd)
        self.open_left_panel(wd)
        wd.find_element_by_css_selector("#button-1059-btnEl").click() #открыть система
        time.sleep(3)
        wd.find_element_by_id("container-1063-innerCt").click()  # клик в пустое место
        time.sleep(3)
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Основные настройки'])[1]/following::span[4]").click() #расширенные настройки
        time.sleep(3)
        wd.find_element_by_xpath("//div[4]/div[4]/div/div").click() #параметры_досье
        time.sleep(3)
        scroll_by = wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Источники данных досье'])[1]/following::span[1]")
        wd.execute_script("arguments[0].scrollIntoView(true);", scroll_by)
        time.sleep(3)
        wd.find_element_by_xpath("//table[@id='treeview-1335-record-2318']/tbody/tr/td/div/span/span[4]").click()
        wd.find_element_by_xpath("//table[@id='treeview-1335-record-2991']/tbody/tr/td[2]/div").click()
        time.sleep(3)

    def open_left_panel(self, wd):
        wd.find_element_by_id("container-1063-innerCt").click()  # клик в пустое место
        element_to_hover_over = wd.find_element_by_css_selector("#button-1046-btnIconEl")  # навести мышку на дом
        hover = ActionChains(wd).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(3)

    def close_redwindow(self, wd):
        wd.find_element_by_xpath("//div[@id='tool-1041-toolEl']").click()  # закрыть окно с ошибкой
        time.sleep(3)

    def login(self, wd):
        wd.find_element_by_id("textfield-1013-inputEl").click()
        wd.find_element_by_id("textfield-1013-inputEl").clear()
        wd.find_element_by_id("textfield-1013-inputEl").send_keys("superadmin")
        wd.find_element_by_id("textfield-1017-inputEl").click()
        wd.find_element_by_id("textfield-1017-inputEl").clear()
        wd.find_element_by_id("textfield-1017-inputEl").send_keys("Zaq1@wsX")
        time.sleep(1)
        wd.find_element_by_xpath(u"//*/text()[normalize-space(.)='Войти']/parent::*").click()
        time.sleep(3)

    def open_dozor(self, wd):
        wd.get("https://10.201.65.116/#dashboard")
        time.sleep(3)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
