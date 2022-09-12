import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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

    def upload_documents(self, name_app1, email_app1, name_app2, email_app2, docfile=False):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            'css selector', self.start_button))).click()
        self.driver.find_element('css selector', self.send_envelope).click()
        time.sleep(10)
        doc_file = "/Users/apparaojajimoggala/DRAFT-CC-2022-003-DocuSign-Regression-PQ.03.docx"
        pdf_file = "/Users/apparaojajimoggala/Computer_System_Validation-converted.pdf"
        self.driver.find_element('css selector', self.upload_file_button).click()
        time.sleep(5)
        browse_button = self.driver.find_element('css selector', self.upload_file_input)
        time.sleep(5)
        if docfile == True:
            browse_button.send_keys(doc_file)
        else:
            browse_button.send_keys(pdf_file)
        time.sleep(10)
        self.driver.find_element('class name', self.set_signing_order).click()
        self.driver.find_element('css selector', self.add_recipients).click()
        time.sleep(5)
        self.driver.find_element('xpath', self.recipient_name1).send_keys(name_app1)
        self.driver.find_element('xpath', self.recipient_email1).send_keys(email_app1)
        self.driver.find_element('xpath', self.recipient_name2).send_keys(name_app2)
        self.driver.find_element('xpath', self.recipient_email2).send_keys(email_app2)
        time.sleep(2)
        self.driver.find_element('css selector', self.next_button).click()
        time.sleep(5)

    def upload_document2(self, name_app1, email_app1, name_app2, email_app2, docfile=False):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((
            'css selector', self.start_button))).click()
        self.driver.find_element('css selector', self.send_envelope).click()
        time.sleep(10)
        doc_file = "/Users/apparaojajimoggala/DRAFT-CC-2022-003-DocuSign-Regression-PQ.03.docx"
        pdf_file = "/Users/apparaojajimoggala/DocuSign-Regression-PQ.pdf"
        self.driver.find_element('css selector', self.upload_file_button).click()
        time.sleep(5)
        browse_button = self.driver.find_element('css selector', self.upload_file_input)
        time.sleep(5)
        if docfile == True:
            browse_button.send_keys(doc_file)
        else:
            browse_button.send_keys(pdf_file)
        time.sleep(10)
        self.driver.find_element('id', self.close_button)
        self.driver.find_element('class name', self.set_signing_order).click()
        self.driver.find_element('css selector', self.add_recipients).click()
        time.sleep(5)
        self.driver.find_element('xpath', self.recipient_name1).send_keys(name_app1)
        self.driver.find_element('xpath', self.recipient_email1).send_keys(email_app1)
        self.driver.find_element('xpath', self.recipient_name2).send_keys(name_app2)
        self.driver.find_element('xpath', self.recipient_email2).send_keys(email_app2)
        time.sleep(2)
        self.driver.find_element('css selector', self.next_button).click()
        time.sleep(5)