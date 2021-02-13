from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random

# DATA BLOCK
HOME_PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/"
LOGIN_OR_REGISTER_PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
password = "QWer-1234!"
confirm_password = password
success_registration_message = "Thanks for registering!"

login_or_register_locator = (By.ID, "login_link")
email_address_locator = (By.ID, "id_registration-email")
password_locator = (By.ID, "id_registration-password1")
confirm_password_locator = (By.ID, "id_registration-password2")
register_button_locator = (By.CSS_SELECTOR, "button[name='registration_submit']")
success_registration_block_locator = (By.CSS_SELECTOR, "div.alertinner")


def generate_unique_email():
    """
    A helper function, which generates a random unique email address, which is required for successful registration.
    :return: str object (uniquely generated username + static domain)
    """
    letters = string.ascii_letters.lower()
    numbers = random.randint(0, 999)
    username = random.choice(letters) + str(numbers)
    domain = "@test.gg"
    return username + domain


def clear_and_complete_input(input_locator: tuple, input_value: str):
    """
    A helper function, which finds, clears and completes an input field
    :param input_locator: tuple object (locator of input web element)
    :param input_value: str object (a value we complete input with)
    """
    input_elem = driver.find_element(*input_locator)
    input_elem.clear()
    input_elem.send_keys(input_value)


def verify_actual_url(expected_url):
    """
    A kind of soft assert function. Is used for unnecessary check of intermediate steps - verifies
    expected url matches with actual one. In case of failure - an exception is raised.
    :param expected_url: str object (url we expect to see)
    *NOTE* Function is created for self-study cases. Actual benefit is controversial.
    """
    current_url = driver.current_url
    if current_url != expected_url:
        raise Exception(f"Current URL is: {current_url}, but expected is: {expected_url}")


try:
    # ARRANGE BLOCK
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    driver.get(HOME_PAGE_URL)
    verify_actual_url(HOME_PAGE_URL)

    login_or_register_elem = driver.find_element(*login_or_register_locator)
    login_or_register_elem.click()
    verify_actual_url(LOGIN_OR_REGISTER_PAGE_URL)

    # ACT BLOCK
    clear_and_complete_input(email_address_locator, generate_unique_email())
    clear_and_complete_input(password_locator, password)
    clear_and_complete_input(confirm_password_locator, confirm_password)

    register_button = driver.find_element(*register_button_locator)
    register_button.click()

    # ASSERT BLOCK
    success_registration_block = driver.find_element(*success_registration_block_locator)
    verify_actual_url(HOME_PAGE_URL)
    assert success_registration_block.text == success_registration_message, "New user registration has failed"
finally:
    driver.quit()
