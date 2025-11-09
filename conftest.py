import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--Incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()