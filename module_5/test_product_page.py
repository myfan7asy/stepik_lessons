import pytest

from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo="


class TestProductPage:
    @pytest.mark.parametrize('promo_offer', ["offer0", "offer1", "offer2", "offer3", "offer4",
                                             "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail),
                                             "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, driver, promo_offer):
        page = ProductPage(driver, link)
        page.open(link + promo_offer)
        page.click_add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.is_product_added_to_cart()
