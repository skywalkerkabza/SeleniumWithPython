from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainResPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.mrdfood.com/'

    def load(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def click_register_button(self):
        register_button = self.driver.find_element(By.ID, 'btnNavRegister')
        register_button.click()

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load(self):
        WebDriverWait(self.driver, 10).until(EC.url_contains('register'))

    def is_register_button_visible(self):
        return self.driver.find_elements(By.ID, 'btnNavRegister')

    def register_user(self, first_name, last_name, email, phone, password):
        self.driver.find_element(By.NAME, "first_name").send_keys(first_name)
        self.driver.find_element(By.NAME, "last_name").send_keys(last_name)
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "phone_1").send_keys(phone)
        self.driver.find_element(By.NAME, "cellmatch").click()
        self.driver.find_element(By.NAME, "cellmatch").send_keys(phone)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "btnNavRegister").click()