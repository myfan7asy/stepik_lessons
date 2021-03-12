from stepik_lessons.module_5.pages.base_page import BasePage
from stepik_lessons.module_5.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert self.is_expected_url_opened("basket")

    def should_be_empty_basket(self):
        self.should_not_be_displayed_product_list()
        self.should_be_visible_empty_basket_note()

    def should_not_be_displayed_product_list(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_LIST), "Product list is present"

    def should_be_visible_empty_basket_note(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_NOTE), "Empty basket note is not displayed"
