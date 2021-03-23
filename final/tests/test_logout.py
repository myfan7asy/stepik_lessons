from final.pages.login_register_page import LoginRegisterPage


class TestLogout:
    def test_logout(self, driver):
        login_page = LoginRegisterPage(driver)
        login_page.open(path="accounts/login/")

        login_page.complete_login_email_address()
        login_page.complete_login_password()
        login_page.click_log_in_button()
        login_page.click_logout()

        login_page.verify_successful_logout()
