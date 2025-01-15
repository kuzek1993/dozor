# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://10.201.64.31/#dashboard")
        driver.find_element_by_id("textfield-1013-inputEl").click()
        driver.find_element_by_id("textfield-1013-inputEl").clear()
        driver.find_element_by_id("textfield-1013-inputEl").send_keys("superadmin")
        driver.find_element_by_id("textfield-1017-inputEl").click()
        driver.find_element_by_id("textfield-1017-inputEl").clear()
        driver.find_element_by_id("textfield-1017-inputEl").send_keys("Zaq1@wsX")
        driver.find_element_by_id("button-1024-btnInnerEl").click()
        driver.find_element_by_id("button-1079-btnIconEl").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()