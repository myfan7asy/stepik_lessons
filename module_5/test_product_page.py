from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestProductPage:
    def test_guest_can_add_product_to_basket(self, driver):
        page = ProductPage(driver, link)
        page.open(link)
        page.should_have_promo_code_in_link()
        page.click_add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.is_product_added_to_cart()

