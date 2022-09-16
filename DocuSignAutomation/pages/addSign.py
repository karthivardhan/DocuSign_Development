import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Add_Sign():
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.signature_field = "button[data-qa='Signature']"
        self.select_approver2 = "button[data-qa='recipient-2']"
        self.send_button = "button[data-qa='footer-send-button']"
        self.home_page = "button[data-qa='header-HOME-tab-button']"
        self.recipient_selector = "button[data-qa='recipient-selector']"

    def add_sign(self):
        driver = self.driver
        source1 = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.signature_field)))
        action = ActionChains(driver)
        action.click_and_hold(source1).move_by_offset(400, 130).pause(2).move_by_offset(-10, -10).release().perform()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, self.recipient_selector).click()
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.select_approver2))).click()
        source1 = self.driver.find_element(By.CSS_SELECTOR, self.signature_field)
        action = ActionChains(driver)
        action.click_and_hold(source1).move_by_offset(650, 130).pause(2).move_by_offset(-10, -10).release().perform()
        time.sleep(10)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.send_button))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.home_page))).click()