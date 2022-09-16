import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages import constants as constants
import pdb
from selenium.webdriver.common.keys import Keys


class Home_Page():
    def __init__(self, driver):
        self.driver = driver

        self.start_button = "button[data-qa='manage-sidebar-actions-ndse-trigger']"
        self.send_envelope = "button[data-qa='manage-sidebar-actions-ndse-send_envelope']"
        self.upload_file = "div[class='css-1d0fnnl']"
        self.upload_file_button = "button[data-qa='upload-file-button']"
        self.browse_button = "label[class='css-rpxvy8']"
        self.add_recipients = "button[data-qa='recipients-add']"
        self.set_signing_order = "focusStyles"
        self.recipient_routing_order1 = "(//input[@data-qa='recipient-routing-order'])[1]"
        self.recipient_routing_order2 = "(//input[@data-qa='recipient-routing-order'])[2]"
        self.recipient_name1 = "(//input[@data-qa='recipient-name'])[1]"
        self.recipient_name2 = "(//input[@data-qa='recipient-name'])[2]"
        self.recipient_email1 = "(//input[@data-qa='recipient-email'])[1]"
        self.recipient_email2 = "(//input[@data-qa='recipient-email'])[2]"
        self.next_button = "button[data-callout='footer-prepare-next-action']"
        self.upload_file_input = "input[data-qa='upload-file-input']"
        self.close_button = "wootric-x"

    def upload_documents(self, name_appr1, email_appr1, name_appr2, email_appr2, docFile=False):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.start_button))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.send_envelope))).click()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.upload_file_button))).click()
        browse_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.upload_file_input)))
        # pdb.set_trace()
        if docFile == True:
            browse_button.send_keys(constants.upload_envelope_docx)
        else:
            browse_button.send_keys(constants.upload_envelope_pdf)
        time.sleep(10)
        self.driver.find_element(By.CLASS_NAME, self.set_signing_order).click()
        self.driver.find_element(By.CSS_SELECTOR, self.add_recipients).click()
        # pdb.set_trace()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_name1))).send_keys(name_appr1)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_email1))).send_keys(email_appr1)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_name2))).send_keys(name_appr2)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_email2))).send_keys(email_appr2)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.next_button))).click()

    def upload_document2(self, name_app1, email_app1, name_app2, email_app2, docfile=False):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, self.start_button))).click()
        self.driver.find_element(By.CSS_SELECTOR, self.send_envelope).click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, self.upload_file_button).click()
        time.sleep(5)
        browse_button = self.driver.find_element(By.CSS_SELECTOR, self.upload_file_input)
        time.sleep(5)
        if docfile == True:
            browse_button.send_keys(constants.upload_envelope_docx)
        else:
            browse_button.send_keys(constants.upload_envelope_pdf)
        time.sleep(10)
        self.driver.find_element(By.ID, self.close_button)
        self.driver.find_element(By.CLASS_NAME, self.set_signing_order).click()
        self.driver.find_element(By.CSS_SELECTOR, self.add_recipients).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.recipient_name1).send_keys(name_app1)
        self.driver.find_element(By.XPATH, self.recipient_email1).send_keys(email_app1)
        self.driver.find_element(By.XPATH, self.recipient_name2).send_keys(name_app2)
        self.driver.find_element(By.XPATH, self.recipient_email2).send_keys(email_app2)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, self.next_button).click()
        time.sleep(5)