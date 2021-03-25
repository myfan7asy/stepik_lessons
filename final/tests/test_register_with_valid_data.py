from final.pages.login_register_page import LoginRegisterPage


class TestRegisterWithValidData:
    # DATA
    login_register_page_path = "accounts/login/"

    def test_register_with_valid_data(self, driver):
        # ACT
        register_page = LoginRegisterPage(driver)
        register_page.open(path=self.login_register_page_path)
        register_page.complete_register_email_address()
        register_page.complete_register_password()
        register_page.complete_register_confirm_password()
        register_page.click_register_button()

        # ASSERT
        register_page.verify_success_registration_message()
