from selenium import webdriver
from loginPage import MainPage, LoginPage
import unittest
import os
os.environ['PATH'] += r"driver/chromedriver"





class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        self.main_page.load()
        self.main_page.click_login_button()

        self.login_page.wait_for_load()
        self.assertFalse(self.login_page.is_login_button_visible(), "Login button is still visible after clicking.")


if __name__ == "__main__":
    unittest.main()
