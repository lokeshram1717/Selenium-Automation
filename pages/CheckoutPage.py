import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID,"first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_summary_amount = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")
        self.confirmation_message = (By.CLASS_NAME, "complete-header")
        self.menu_button = (By.ID,"react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")

    def enter_shipping_details(self,firstname,lastname,postalcode):
        self.driver.find_element(*self.first_name).send_keys(firstname)
        self.driver.find_element(*self.last_name).send_keys(lastname)
        self.driver.find_element(*self.postal_code).send_keys(postalcode)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def total_amount(self):
        return self.driver.find_element(*self.total_summary_amount).text

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def get_confirmation_message(self):
        return self.driver.find_element(*self.confirmation_message).text

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.logout_button))
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.logout_button)).click()