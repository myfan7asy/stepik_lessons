from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, driver):
        page = MainPage(driver, link)
        page.open(link)
        page.go_to_login_page()
