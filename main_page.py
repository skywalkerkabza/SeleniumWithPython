from selenium.webdriver.common.by import By

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
