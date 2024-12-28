# -*- coding: utf-8 -*-
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
        wd.find_element_by_id("button-1051-btnIconEl").click()
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Solar Dozor'])[2]/following::*[name()='svg'][2]").click()
        wd.find_element_by_css_selector("nz-tree-node-switcher.ant-tree-switcher.ng-star-inserted.ant-tree-switcher_open > i.anticon.anticon-down.ant-tree-switcher-icon.ng-star-inserted > svg").click()
        wd.find_element_by_xpath("//app-agents-zone[@id='ext-element-155']/div/div/app-agents-tree/div/nz-tree/div[2]/div/cdk-virtual-scroll-viewport/div/nz-tree-node[5]/nz-tree-node-switcher").click()
        wd.find_element_by_xpath("//app-agents-zone[@id='ext-element-155']/div/div/app-agents-tree/div/nz-tree/div[2]/div/cdk-virtual-scroll-viewport/div/nz-tree-node[5]/nz-tree-node-switcher").click()

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
        time.sleep(3)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
