from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

class WebdriverUtil:
    def __init__(self,driver):
        self.driver = driver

    def wait_for_element_visible(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            return None

    def click_element(self,locator,timeout=10):
        try:
            element = self.wait_for_element_visible(locator, timeout)
            element.click()
        except (TimeoutException, ElementClickInterceptedException):
            return None

