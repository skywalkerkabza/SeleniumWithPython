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


class TestLogin:
    def __init__(self, driver):
        self.driver = driver

    def test_login(self):
        # Navigate to the main page and click on the login button
        main_page = MainPage(self.driver)
        main_page.load()
        main_page.click_login_button()

        # Wait for the login page to load
        login_page = LoginPage(self.driver)
        login_page.wait_for_load()

        # Assert that the login button is no longer visible
        assert not login_page.is_login_button_visible(), "Login button still visible after clicking."

        # Perform login steps (replace with actual login process)
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("your_username")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("your_password")
        self.driver.find_element(By.ID, 'btnLogin').click()

        # Add more steps as needed for your login process

        # Example logout (replace with actual logout process)
        self.driver.find_element(By.ID, "menu_btn").click()
        self.driver.find_element(By.NAME, "Sign Out").click()
