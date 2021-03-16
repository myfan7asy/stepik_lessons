from stepik_lessons.module_5.pages.base_page import BasePage
from stepik_lessons.module_5.pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_expected_url_opened("login")

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        login_input = self.driver.find_element(*LoginPageLocators.login_input)
        login_input.send_keys(email)
        password_input = self.driver.find_element(*LoginPageLocators.password_input)
        password_input.send_keys(password)
        confirm_password_input = self.driver.find_element(*LoginPageLocators.confirm_password_input)
        confirm_password_input.send_keys(password)
        login_button = self.driver.find_element(*LoginPageLocators.register_button)
        login_button.click()
