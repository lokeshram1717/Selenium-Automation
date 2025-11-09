import selenium
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME,"shopping_cart_link")
        self.cart_item_name = (By.CLASS_NAME,"inventory_item_name")
        self.checkout_button = (By.ID,"checkout")

    def add_product_to_cart(self,product_name):
        formatted_name = product_name.lower().replace(" ", "-")
        button_id = f"add-to-cart-{formatted_name}"
        self.driver.find_element(By.ID, button_id).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_link).click()

    def get_cart_item_name(self):
        return self.driver.find_element(*self.cart_item_name).text

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()
