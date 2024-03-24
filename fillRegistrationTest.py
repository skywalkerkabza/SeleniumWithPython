from selenium import webdriver
from registerPage import MainResPage, RegisterPage
import unittest
import json
import os
os.environ['PATH'] += r"driver/chromedriver"
class RegisterPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainResPage(self.driver)
        self.register_page = RegisterPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_register_user(self):
        self.main_page.load()
        self.main_page.click_register_button()

        self.register_page.wait_for_load()

        # Read user data from a JSON file
        try:
            with open('user_data.json', 'r') as file:
                users = json.load(file)
                for user in users:
                    first_name = user['first_name']
                    last_name = user['last_name']
                    email = user['email']
                    phone = user['phone']
                    password = user['password']
                    self.register_page.register_user(first_name, last_name, email, phone, password)


        except json.decoder.JSONDecodeError as e:
            self.fail(f"Failed to load user data from JSON file: {e}")

if __name__ == "__main__":
    unittest.main()