import csv
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages import constants as constants

class Util_Test():
    def __init__(self, driver):
        self.driver = driver

        # Locators:
        self.profile_button = "button[data-qa='header-profile-menu-button']"
        self.logoff_button = "button[data-qa='header-logoff-button']"

    def read_data_from_csv(self, filename):
        with open(filename, 'r') as file:
            csvFile = csv.DictReader(file)
            for lines in csvFile:
                print(lines)
                assert "Sent On (Date)" in lines
                assert "Sent On (Time)" in lines
        self.driver.save_screenshot(constants.screenshot+'/Envelope_csv_report.png')

    def logout(self):
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.profile_button))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.logoff_button))).click()

    def scroll_page(self):
        self.driver.find_element('css selector', "button[data-qa='tutorial-got-it']").click()
        time.sleep(5)
        self.driver.execute.script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    def switch_to_window(self):
        parentWindow = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
                yield
        self.driver.switch_to.window(parentWindow)