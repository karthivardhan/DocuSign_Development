import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pages.loginPage import Login_Page
from pages import constants as constants


class Approve_Documnets():
    def __init__(self, driver):
        self.driver = driver

        # Elements:
        self.manage_tab = "button[data-qa='header-MANAGE-tab-button']"
        self.action_required = "button[data-qa='action-required-count']"
        self.select_envelope = "//div[contains(text(), "+constants.envelope_name+")]"
        self.sign_button = "button[data-qa='status-action-button-sign']"
        self.continue_button = "action-bar-btn-continue"
        self.navigate_option = "navigate-btn"
        self.sign_option = "//*[contains(@class, 'signature-tab-content')]"
        self.signing_reason = "signingReason"
        self.select_signing_reason = "//*[contains(text(),'I approve')]"
        self.dialog_submit = "button[data-qa='dialog-submit']"
        self.cfr_continue = "button[data-qa='cfr-continue']"
        self.finish_button = "action-bar-btn-finish"
        self.no_thanks_button = "button[data-qa='sign-next-no-thanks']"

    def approve_document(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(('css selector', self.action_required))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(('xpath', self.select_envelope))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(('css selector', self.sign_button))).click()

    def sign_approver1(self):
        driver = self.driver
        self.driver.find_element('id', self.continue_button).click()
        self.driver.find_element('id', self.navigate_option).click()
        self.driver.find_element('xpath', self.sign_option).click()
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        drop_down = self.driver.find_element('id', self.signing_reason)
        select_method = Select(drop_down)
        select_method.select_by_visible_text('I approve this document')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(('css selector', self.dialog_submit))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(('css selector', self.cfr_continue))).click()
        all_windows = self.driver.window_handles
        current_window = all_windows[0]
        new_window = all_windows[1]
        self.driver.switch_to.window(new_window)
        time.sleep(5)
        login = Login_Page(driver)
        login.login_page(constants.approver1Email, constants.approver1Password)
        self.driver.switch_to.window(current_window)
        time.sleep(2)

    def sign_approver2(self):
        driver = self.driver
        self.driver.find_element('id', self.continue_button).click()
        self.driver.find_element('id', self.navigate_option).click()
        self.driver.find_element('xpath', self.sign_option).click()
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        drop_down = self.driver.find_element('id', self.signing_reason)
        select_method = Select(drop_down)
        select_method.select_by_visible_text('I approve this document')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(('css selector', self.dialog_submit))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(('css selector', self.cfr_continue))).click()
        time.sleep(5)
        all_windows = self.driver.window_handles
        current_window = all_windows[0]
        new_window = all_windows[1]
        self.driver.switch_to.window(new_window)
        time.sleep(5)
        login = Login_Page(driver)
        login.login_page(constants.approver2Email, constants.approver2Password)
        self.driver.switch_to.window(current_window)
        time.sleep(2)

    def complete_sign(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(('id', self.finish_button))).click()
        time.sleep(20)
        main_window2 = self.driver.window_handles
        for handle2 in self.driver.window_handles:
            if handle2 != main_window2:
                popup2 = handle2
                self.driver.switch_to.window(popup2)
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(('css selector', self.no_thanks_button))).click()