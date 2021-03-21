from selenium.webdriver.common.by import By

from final.helpers.generators import generate_unique_email
from final.pages.base_page import BasePage


class LoginPage(BasePage):
    unique_email = generate_unique_email()
    password = "QWer-1234!"
    confirm_password = password
    success_registration_message = "Thanks for registering!"

    email_address_locator = (By.ID, "id_registration-email")
    password_locator = (By.ID, "id_registration-password1")
    confirm_password_locator = (By.ID, "id_registration-password2")
    register_button_locator = (By.CSS_SELECTOR, "button[name='registration_submit']")
    success_registration_block_locator = (By.CSS_SELECTOR, "div.alertinner")

    def complete_email_address(self):
        self.find_text_input_and_complete_it(self.email_address_locator, self.unique_email)

    def complete_password(self):
        self.find_text_input_and_complete_it(self.password_locator, self.password)

    def complete_confirm_password(self):
        self.find_text_input_and_complete_it(self.confirm_password_locator, self.password)

    def click_register_button(self):
        self.find_element_and_click_on_it(self.register_button_locator)

    def verify_success_registration_message(self):
        success_registration_block = self.driver.find_element(*self.success_registration_block_locator)
        assert success_registration_block.text == self.success_registration_message, \
            "New user registration has failed"
