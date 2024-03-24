import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from main_page import MainPage
from login_page import LoginPage
import os

os.environ['PATH'] += r"driver/chromedriver"


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        main_page = MainPage(self.driver)
        main_page.load()
        main_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.wait_for_load()

        self.assertFalse(login_page.is_login_button_visible(), "Login button still visible after clicking.")

        # Perform login steps (replace with actual login process)
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("kabelo.modipa@allangray.co.za")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("Vodacom20!8")
        self.driver.find_element(By.ID, 'btnLogin').click()

        # Example logout (replace with actual logout process)
        # self.driver.find_element(By.ID, "menu_btn").click()
        # self.driver.find_element(By.NAME, "Sign Out").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
