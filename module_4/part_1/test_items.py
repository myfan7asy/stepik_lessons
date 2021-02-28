from helper import *
from selenium.webdriver.common.by import By

# Data block
PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
add_to_bag_locator = (By.CSS_SELECTOR, "button.btn-add-to-basket")


def test_open_url_and_verify_button_text(driver, language):
    # Arrange block
    driver.get(PRODUCT_URL)

    # Act block
    add_to_cart_button = driver.find_element(*add_to_bag_locator)

    # Assert block
    assert add_to_cart_button.text == locales[f"{language}"], "Button text is not as expected"
