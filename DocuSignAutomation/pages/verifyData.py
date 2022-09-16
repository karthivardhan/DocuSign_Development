import logging

import PyPDF2
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages import constants as constants
from selenium import webdriver
import urllib.request
from urllib import request
from urllib.request import Request, urlopen
import time
from urllib.error import HTTPError, URLError
from socket import timeout


class Verify_Data():
    def __init__(self, driver):
        self.driver = driver
        self.ww = WebDriverWait(self.driver, 20)

        # Locators:
        self.manage_tab = "button[data-qa='header-MANAGE-tab-button']"
        self.sent_box = "button[data-qa='manage-sidebar-labels-sent-label']"
        self.select_envelope_docx = "//div[contains(text(), " + constants.envelope_file_docx + ")]"
        self.open_document = "//a[@data-qa='page-thumbnail']"
        self.more_document = "button[data-qa='document-more']"
        self.envelope_action_history = "button[data-qa='envelope-action-history']"
        self.history_activity_row = "tr[data-qa='history-activity-row']"
        self.user_name_text = "(//td[contains(text(), 'Docusign Sender')])[1]"
        self.signature_id = "//td[contains(text(), '54cfffe6-35eb-4dd9-81e8-35ab08e0e62e')]"
        self.adopted_signature_id = "//td[contains(text(), '723bde61-2321-43f8-af2a-4d5a04843d65')]"
        self.close_button = "//button[@data-qa='history-modal-close']"
        self.reports_tab = "//button[@data-qa='header-REPORTS-tab-button']"
        self.envelope_option = "//div[@data-qa='Envelope']"
        self.view_button = "(//button[@data-qa='report-action'])[1]"
        self.report_range_menu = "button[data-qa='report-range-menu']"
        self.date_range_any = "button[data-qa='date_range_any']"
        self.run_report = "button[data-qa='run-report']"
        self.report_result = "(//tr[@data-qa='report-result-row'])[1]"
        self.report_download = "//button[@data-qa='report-download-icon']"

    # Verify date format on Envelope
    def verify_data(self):
        self.ww.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.manage_tab))).click()
        self.ww.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sent_box))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_envelope_docx))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.open_document))).click()
        time.sleep(10)
        parentWindow = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                childWindow = handle
                self.driver.switch_to.window(childWindow)
        self.driver.save_screenshot(
            constants.screenshot + "/date_format.png")
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(parentWindow)
        # time.sleep(10)
        # # pdb.set_trace()
        # url = self.driver.current_url
        # try:
        #     req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        #     webpage = urlopen(req).read()
        #     print(webpage)
        # except HTTPError as error:
        #     logging.error('HTTP Error')
        # except URLError as error:
        #     if isinstance(error.reason, timeout):
        #         logging.error('Timeout Error')
        #     else:
        #         logging.error('URL Error')
        # else:
        #     logging.info('Access successful.')

        # print(pdfData)
        # with urllib.request.urlopen(self.driver.current_url) as pdfDataFile:
        #     pdfData = pdfDataFile.read().decode('utf-8')
        #     print(pdfData)
        # pdfReader = PyPDF2.PdfFileReader(pdfDataFile)
        # print(pdfReader.numPages)
        # pageObject = pdfReader.getPage(0)
        # print(pageObject.extractText())
        # for pdfData in pdfReader:
        #     print(pdfData)
        # self.driver.switch_to.window(parentWindow)

    # Verify Envelope history
    def envelope_history(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.manage_tab))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sent_box))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_envelope_docx))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.more_document))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.envelope_action_history))).click()
        parentWindow = self.driver.current_window_handle
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        self.driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(10)
        text_userName = self.driver.find_element(By.XPATH, self.user_name_text).text
        print(text_userName)
        text_signatureID = self.driver.find_element(By.XPATH, self.signature_id).text
        print(text_signatureID)
        self.driver.find_element(By.XPATH, self.close_button).click()
        self.driver.switch_to.window(parentWindow)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.reports_tab))).click()
        # pdb.set_trace()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.envelope_option))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.view_button))).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.report_range_menu))).click()
        self.ww.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.date_range_any))).click()
        self.ww.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.run_report))).click()
        report_result = self.ww.until(EC.element_to_be_clickable((By.XPATH, self.report_result))).text
        print(report_result)
        download = self.ww.until(EC.element_to_be_clickable((By.XPATH, self.report_download)))
        self.driver.execute_script("arguments[0].click();", download)