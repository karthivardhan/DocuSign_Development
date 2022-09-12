import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_Page():
    def __init__(self, driver):
        self.driver = driver

        self.user_name = "input[data-qa='username']"
        self.submit_userName = "button[data-qa='submit-username']"
        self.password = "input[data-qa='password']"
        self.submit_password = "button[data-qa='submit-password']"
        self.home_page_title = "header-home-desktop"

    def login_page(self, userName, password):
        self.driver.find_element('css selector', self.user_name).send_keys(userName)
        self.driver.find_element('css selector', self.submit_userName).click()
        self.driver.find_element('css selector', self.password).send_keys(password)
        self.driver.find_element('css selector', self.submit_password).click()
        time.sleep(20)
