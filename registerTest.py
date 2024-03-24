from selenium import webdriver
from registerPage import MainResPage, RegisterPage
import unittest
import os

os.environ['PATH'] += r"driver/chromedriver"


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainResPage(self.driver)
        self.register_page = RegisterPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_register(self):
        self.main_page.load()
        self.main_page.click_register_button()

        self.register_page.wait_for_load()
        self.assertFalse(self.register_page.is_register_button_visible(),
                         "Register button is still visible after clicking.")


if __name__ == "__main__":
    unittest.main()
