from final.pages.login_page import LoginPage


class TestRegisterWithValidData:
    login_page_path = "accounts/login/"

    def test_register_with_valid_data(self, driver):
        login_page = LoginPage(driver)
        login_page.open(path=self.login_page_path)
        login_page.complete_email_address()
        login_page.complete_password()
        login_page.complete_confirm_password()
        login_page.click_register_button()
        login_page.verify_success_registration_message()
