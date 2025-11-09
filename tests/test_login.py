from pages.LoginPage import LoginPage

def test_valid_Page(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    assert "inventory" in driver.current_url


def test_invalid_Page(setup):
    driver =setup
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    login_page.enter_username("wrong_user")
    login_page.enter_password("wrong_pass")
    login_page.click_login()
    error_text = login_page.get_error_message()
    assert "Username and password do not match" in error_text




