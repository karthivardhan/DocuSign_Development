from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

my_element_id = 'something123'
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
your_element = WebDriverWait(your_driver, some_timeout,ignored_exceptions=ignored_exceptions)\
                        .until(expected_conditions.presence_of_element_located((By.ID, my_element_id)))