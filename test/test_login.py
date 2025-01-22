# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options

class CheckLdap(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:\\Users\\v.kochergin\\AppData\\Local\\Mozilla Firefox\\firefox.exe'
        self.wd = webdriver.Firefox(executable_path=r'C:\\Users\\v.kochergin\\Downloads\\geckodriver.exe', options=options)
        self.wd.implicitly_wait(30)

    def test_connect_ldap(self):
        wd = self.wd
        self.open_dozor(wd)
        self.login(wd)
        #self.close_redwindow(wd)
        self.open_left_panel(wd)
        wd.find_element_by_xpath("//a[14]/span/span").click() #открыть система
        time.sleep(3)
        wd.find_element_by_xpath("//div[3]/div/div/div[2]/div").click()  # клик в пустое место
        time.sleep(3)
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Основные настройки'])[1]/following::span[4]").click() #расширенные настройки
        time.sleep(3)
        wd.find_element_by_xpath("//div[4]/div[4]/div/div").click() #параметры_досье
        time.sleep(3)
        scroll_by = wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Источники данных досье'])[1]/following::span[1]")
        wd.execute_script("arguments[0].scrollIntoView(true);", scroll_by) #скрол к источникам досье
        time.sleep(3)
        wd.find_element_by_xpath(u"//*/text()[normalize-space(.)='Добавить']/parent::*").click() #клик на кнопку добавить
        time.sleep(3)
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Название источника'])[5]/following::div[1]").click() #клик на название источника
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").send_keys("test")  # задать_название
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='DN пользователя'])[1]/following::div[1]").click() # задать_DN
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").send_keys("administrator@isim.local")
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Пароль пользователя'])[1]/following::div[1]").click() # задать_пароль
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").send_keys("1qaz@WSX")
        time.sleep(3)
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='URL LDAP сервера'])[1]/following::div[1]").click() # задать_сервер
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").send_keys("ldap://10.199.29.96:389")
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Базовый DN для поиска'])[1]/following::div[1]").click() # задать_dn_для_поиска
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").send_keys("OU=pilot-users,OU=Employees,dc=isim,dc=local")
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Число записей на странице'])[1]/following::div[1]").click() # число_записей
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").send_keys("100")
        time.sleep(3)
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Фильтр подразделений'])[1]/following::div[1]").click() # подразделения
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").send_keys("(objectCategory=organizationalUnit)")
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Фильтр групп'])[1]/following::div[1]").click() # группы
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").send_keys("(objectCategory=group)")
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Фильтр персон'])[1]/following::div[1]").click() # персоны
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[2]/div/div/div/div/input").send_keys(
            "(&(objectCategory=person)(objectClass=user))")
        time.sleep(3)
        wd.find_element_by_xpath(u"//*/text()[normalize-space(.)='Проверить']/parent::*").click()
        time.sleep(3)
        wd.find_element_by_xpath(u"//*/text()[normalize-space(.)='Сохранить']/parent::*").click()  # сохранить
        time.sleep(3)
        wd.find_element_by_xpath(u"//*/text()[normalize-space(.)='Применить']/parent::*").click() # применить
        time.sleep(3)
        wd.find_element_by_xpath("//div[2]/div/div/div/div/div/div[2]/div/div/a/span/span/span[2]").click() # применить еще раз
        time.sleep(13)
        scroll_by = wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Источники данных досье'])[1]/following::span[1]")
        wd.execute_script("arguments[0].scrollIntoView(true);", scroll_by)  # скрол к источникам досье
        time.sleep(3)
        wd.find_element_by_xpath(u"//*/text()[normalize-space(.)='Синхронизировать']/parent::*").click()
        time.sleep(50)


    def open_left_panel(self, wd):
        wd.find_element_by_xpath("//div[3]/div/div/div[2]/div").click()  # клик в пустое место
        element_to_hover_over = wd.find_element_by_xpath("//span/span/span")  # навести мышку на дом
        hover = ActionChains(wd).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(3)

    #def close_redwindow(self, wd):
        #wd.find_element_by_xpath("//div[@id='tool-1041-toolEl']").click()  # закрыть окно с ошибкой
        #time.sleep(3)

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
