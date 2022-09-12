# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(10)
# driver.get("https://the-internet.herokuapp.com/upload");
# get_title = driver.title
# print(get_title)
# driver.find_element('id', "file-upload").send_keys("/Users/apparaojajimoggala/DRAFT-CC-2022-003-DocuSign-Regression-PQ.03.docx")
# time.sleep(20)
# driver.find_element('id', "file-submit").submit()
# if driver.page_source.find("File Uploaded!"):
#     print("file upload success")
# else:
#     print("file upload not successful")
# driver.quit()
#
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
# from selenium.webdriver import ActionChains
import unittest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# set chromodriver.exe path
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver.implicitly_wait(0.5)
# #launch URL
# driver.get("https://www.tutorialspoint.com/index.htm")
# #scroll to page end with JavaScript Executor
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(10)
# #identify element at page end
# m = driver.find_element_by_xpath("//h3[text()='Contact Us']")
# #get element text
# s = m.text
# print("Text is: ")
# print(s)
# close browser
# driver.quit()

'''class Unit:
    def __init__(self, driver):
        self.driver = driver

    def test_drag_drop(self):
        driver = self.driver
        driver = webdriver.Chrome()
        driver.get('https://jqueryui.com/draggable/')
        driver.maximize_window()
        driver.switch_to.frame(0)
        source1 = driver.find_element_by_id('draggable')
        action = ActionChains(driver)
        action.click_and_hold(source1).move_by_offset(150, 100).pause(2).move_by_offset(-10, -10).release().perform()
        print("Dragging & dropping test case successful\n")
        time.sleep(5)


obj = Unit()
obj.test_drag_drop(driver)'''
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://jqueryui.com/draggable/')
driver.maximize_window()
driver.switch_to.frame(0)
source1 = driver.find_element('id', 'draggable')
action = ActionChains(driver)
action.click_and_hold(source1).move_by_offset(500, 100).pause(2).move_by_offset(-10, -10).release().perform()
time.sleep(10)
print("Dragging & dropping test case successful\n")
time.sleep(5)
