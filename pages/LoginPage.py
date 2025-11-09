import selenium
from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username = (By.NAME,"user-name")
        self.password = (By.NAME, "password")
        self.login_button = (By.NAME,"login-button")
        self.error_message = (By.XPATH,"//h3[@data-test='error']")


    def enter_username(self,username):
        self.driver.find_element(*self.username).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def handle_alert_if_present(self,timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            print("Alert text: ",alert.text)
            alert.accept()
        except TimeoutException:
            print("No alert appeared within timeout.")
        except NoAlertPresentException:
            print("No alert present at this moment.")
        except Exception as e:
            print(f"Unexpected alert handling issue: {e}")

