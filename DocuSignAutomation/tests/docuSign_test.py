from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from pages import constants as constants
from pages.addSign import Add_Sign
from pages.approveDocument import Approve_Documnets
from pages.auditLogs import Audit_Logs
from pages.verifyData import Verify_Data
from utilities.utils import Util_Test
import pytest


@pytest.mark.usefixtures("test_setup")
class TestNew():
    def test_loginPage(self):
        driver = self.driver
        self.driver.get(constants.baseUrl)
        self.driver.delete_all_cookies()
        login = Login_Page(driver)
        login.login_page(constants.senderEmail, constants.senderPassword)
        home = Home_Page(driver)
        home.upload_documents(
            constants.approver1Name, constants.approver1Email, constants.approver2Name, constants.approver2Email,
            True)
        # scroll = Scroll(driver)
        # scroll.scroll_page()
        sign = Add_Sign(driver)
        sign.add_sign()

        # Upload pdf file
        home = Home_Page(driver)
        home.upload_documents(
            constants.approver1Name, constants.approver1Email, constants.approver2Name, constants.approver2Email, False)
        sign = Add_Sign(driver)
        sign.add_sign()
        user = Util_Test(driver)
        user.logout()

        # Login as approver1 and complete sign
        self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.approver1Email, constants.approver1Password)
        approve = Approve_Documnets(driver)
        approve.approve_document(True)
        login = Login_Page(driver)
        login.login_page(constants.approver1Email, constants.approver1Password)
        sign = Approve_Documnets(driver)
        sign.sign_approver1()
        complete = Approve_Documnets(driver)
        complete.complete_sign_approver1()
        user = Util_Test(driver)
        user.logout()

        # Login as approver2 and complete sign
        self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.approver2Email, constants.approver2Password)
        approve = Approve_Documnets(driver)
        approve.approve_document(True)
        login = Login_Page(driver)
        login.login_page(constants.approver2Email, constants.approver2Password)
        sign = Approve_Documnets(driver)
        sign.sign_approver2()
        complete = Approve_Documnets(driver)
        complete.complete_sign_approver2()
        user = Util_Test(driver)
        user.logout()

        # Verify data:
        self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.senderEmail, constants.senderPassword)
        data = Verify_Data(driver)
        data.verify_data()

        # Verify Envelope history
        data.envelope_history()

        # Verify Audit logs
        logs = Audit_Logs(driver)
        logs.auditLogs()
        csv = Util_Test(driver)
        csv.read_data_from_csv(constants.csv_envelope_report)