from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


class TestHomePageInteractions:
    path = "en-gb/"
    login_page_path = "accounts/login/"
    basket_page_path = "basket/"

    def test_open_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.verify_url(self.path)

    def test_open_login_page_from_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.open_login_page()

        login_page = LoginPage(driver)
        login_page.verify_url(self.login_page_path)

    def test_open_empty_basket_from_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        home_page.open_basket_page()

        basket_page = BasketPage(driver)
        basket_page.verify_url(self.basket_page_path)
        basket_page.is_basket_empty()
