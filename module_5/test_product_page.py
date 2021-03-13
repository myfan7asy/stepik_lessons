import pytest

from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

promo_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo="
product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"


class TestProductPage:
    @pytest.mark.parametrize('promo_offer', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5",
                                             "offer6", pytest.param("offer7", marks=pytest.mark.xfail),
                                             "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, driver, promo_offer):
        page = ProductPage(driver, promo_link)
        page.open(promo_link + promo_offer)
        page.click_add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.is_product_added_to_cart()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, driver):
        page = ProductPage(driver, product_link)
        page.open(product_link)
        page.click_add_to_basket_button()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, driver):
        page = ProductPage(driver, product_link)
        page.open(product_link)
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, driver):
        page = ProductPage(driver, product_link)
        page.open(product_link)
        page.click_add_to_basket_button()
        page.should_be_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, driver):
        page = ProductPage(driver, product_link)
        page.open(product_link)
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, driver):
        page = ProductPage(driver, product_link)
        page.open(product_link)
        page.go_to_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, driver):
        page = ProductPage(driver, product_link)
        page.open(product_link)
        page.go_to_basket_page()
        basket_page = BasketPage(driver, driver.current_url)
        basket_page.should_be_basket_url()
        basket_page.should_be_empty_basket()


@pytest.mark.xfail
@pytest.mark.registered_user
class TestUserAddToBasketFromProductPage:
    def test_user_should_see_login_link_on_product_page(self, setup, driver):
        page = ProductPage(driver, product_link)
        page.open(product_link)

    def test_user_can_add_product_to_basket(self, setup, driver):
        page = ProductPage(driver, product_link)
        page.open(product_link)
        page.click_add_to_basket_button()
        page.is_product_added_to_cart()
