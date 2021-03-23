from selenium.webdriver.common.by import By

from final.helpers.credentials import valid_login_credentials
from final.helpers.generators import generate_unique_email
from final.pages.base_page import BasePage


class LoginRegisterPage(BasePage):
    """
    A class-container for Login/Register page. Is a child to BasePage.
    Contains page specific fields (data and locators) as well as methods.
    """
    # Log In block
    success_login_message = "Welcome back"

    login_email_address_locator = (By.ID, "id_login-username")
    login_password_locator = (By.ID, "id_login-password")
    login_button_locator = (By.CSS_SELECTOR, "button[name='login_submit']")
    success_login_block_locator = (By.CSS_SELECTOR, "div.wicon")

    # Register block
    unique_email = generate_unique_email()
    password = "QWer-1234!"
    confirm_password = password
    success_registration_message = "Thanks for registering!"

    register_email_address_locator = (By.ID, "id_registration-email")
    register_password_locator = (By.ID, "id_registration-password1")
    register_confirm_password_locator = (By.ID, "id_registration-password2")
    register_button_locator = (By.CSS_SELECTOR, "button[name='registration_submit']")
    success_registration_block_locator = (By.CSS_SELECTOR, "div.alertinner")

    def complete_register_email_address(self):
        self.find_text_input_and_complete_it(self.register_email_address_locator, self.unique_email)

    def complete_register_password(self):
        self.find_text_input_and_complete_it(self.register_password_locator, self.password)

    def complete_register_confirm_password(self):
        self.find_text_input_and_complete_it(self.register_confirm_password_locator, self.password)

    def click_register_button(self):
        self.find_element_and_click_on_it(self.register_button_locator)

    def verify_success_registration_message(self):
        success_registration_block = self.driver.find_element(*self.success_registration_block_locator)
        assert success_registration_block.text == self.success_registration_message, \
            "New user registration has failed"

    def complete_login_email_address(self):
        self.find_text_input_and_complete_it(self.login_email_address_locator, valid_login_credentials['email'])

    def complete_login_password(self):
        self.find_text_input_and_complete_it(self.login_password_locator, valid_login_credentials['password'])

    def click_log_in_button(self):
        self.find_element_and_click_on_it(self.login_button_locator)

    def verify_success_login_message(self):
        success_login_block = self.driver.find_element(*self.success_login_block_locator)
        assert success_login_block.text == self.success_login_message, \
            "User login has failed"

    def verify_account_link(self):
        assert self.is_element_present(self.account_link_locator), \
            "Account link is not visible"

    def verify_logout_link(self):
        assert self.is_element_present(self.logout_link_locator), \
            "Logout link is not visible"

    def is_user_logged_in(self):
        self.verify_success_login_message()
        self.verify_account_link()
        self.verify_logout_link()
