import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestMainPage:
    def test_guest_can_go_to_login_page(self, driver):
        page = MainPage(driver, link)
        page.open(link)
        page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, driver):
        page = MainPage(driver, link)
        page.open(link)
        page.go_to_basket_page()
        basket_page = BasketPage(driver, driver.current_url)
        basket_page.should_be_basket_url()
        basket_page.should_be_empty_basket()
