from helper import *
from selenium.webdriver.common.by import By

PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_open_url_and_verify_button_text(driver, language):
    driver.get(PRODUCT_URL)
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, f"button[value='{locales[f'{language}']}']")
    assert add_to_cart_button.text == locales[f"{language}"], "Button text is not as expected"
