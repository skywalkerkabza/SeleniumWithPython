from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.mrdfood.com/'

    def load(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def click_login_button(self):
        login_button = self.driver.find_element(By.ID, 'btnNavLogin')
        login_button.click()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains('login'))

    def is_login_button_visible(self):
        return self.driver.find_elements(By.ID, 'btnNavLogin')
