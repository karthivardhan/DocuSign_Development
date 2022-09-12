import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope='class')
def test_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    driver.implicitly_wait(3)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # driver.quit()


class Scroll():
    def __init__(self, driver):
        self.driver = driver

    def scroll_page(self):
        self.driver.find_element('css selector', "button[data-qa='tutorial-got-it']").click()
        # self.driver.find_element('css selector', 'c241').click()
        # self.driver.find_element('css selector', "[class='css-1nsshgk']").click()
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)

    def logout(self):
        self.driver.find_element("css selector", "button[data-qa='header-profile-menu-button']").click()
        self.driver.find_element('css selector', "button[data-qa='header-logoff-button']").click()
        time.sleep(10)
