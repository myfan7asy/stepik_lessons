from .login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, driver):
        page = MainPage(driver, link)
        page.open(link)
        page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()
