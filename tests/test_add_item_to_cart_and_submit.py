import pytest

from pages.LoginPage import LoginPage
from pages.CheckoutPage import CheckoutPage
from pages.HomePage import HomePage
from util.data_reader import get_test_data

test_data = get_test_data("Data/test_data.csv")


@pytest.mark.parametrize("data", test_data)
def test_add_item_to_cart_and_submit_page(setup, data):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    #login
    login_page = LoginPage(driver)
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()
    login_page.handle_alert_if_present()
    assert "inventory" in driver.current_url


    #add item to cart
    home_page = HomePage(driver)
    home_page.add_product_to_cart(data["product_name"])
    home_page.open_cart()
    login_page.handle_alert_if_present()
    assert data["product_name"] == home_page.get_cart_item_name()
    home_page.checkout()


    # add details and submit the order

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_shipping_details(data["firstname"],data["lastname"],data["zipcode"])
    checkout_page.click_continue()
    assert "10" in checkout_page.total_amount()
    checkout_page.click_finish()
    assert "Thank you for your order" in checkout_page.get_confirmation_message()
    checkout_page.logout()