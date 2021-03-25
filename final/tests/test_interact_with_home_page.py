from final.pages.home_page import HomePage
from final.pages.login_register_page import LoginRegisterPage
from final.pages.basket_page import BasketPage


class TestHomePageInteractions:
    # DATA
    path = "en-gb/"
    login_page_path = "accounts/login/"
    basket_page_path = "basket/"

    def test_open_home_page(self, driver):
        # ARRANGE
        home_page = HomePage(driver)

        # ACT
        home_page.open()

        # ASSERT
        home_page.verify_url(self.path)

    def test_open_login_page_from_home_page(self, driver):
        # ARRANGE
        home_page = HomePage(driver)
        home_page.open()

        # ACT
        home_page.open_login_page()

        # ASSERT
        login_page = LoginRegisterPage(driver)
        login_page.verify_url(self.login_page_path)

    def test_verify_empty_basket_opened_from_home_page_has_no_products(self, driver):
        # ARRANGE
        home_page = HomePage(driver)
        home_page.open()

        # ACT
        home_page.open_basket_page()

        # ASSERT
        basket_page = BasketPage(driver)
        basket_page.verify_url(self.basket_page_path)
        basket_page.is_basket_empty()
