from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_google_search():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium python")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)
    print("Page title after search", driver.title)

    driver.quit()

