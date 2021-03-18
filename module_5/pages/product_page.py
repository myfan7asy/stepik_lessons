from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        add_to_basket_button = self.driver.find_element(*ProductPageLocators.add_to_basket_button)
        add_to_basket_button.click()

    def is_success_message_displayed(self):
        book_name = self.driver.find_element(*ProductPageLocators.product_name).text
        success_message = self.driver.find_element(*ProductPageLocators.success_message_with_product_name).text
        assert book_name == success_message, "Success message displays wrong book name"

    def is_basket_has_correct_total(self):
        book_price = self.driver.find_element(*ProductPageLocators.product_price).text
        basket_message = self.driver.find_element(*ProductPageLocators.basket_message_with_product_price).text
        assert book_price == basket_message, "Cart Price does not match with Book Price"

    def is_product_added_to_cart(self):
        self.is_basket_has_correct_total()
        self.is_success_message_displayed()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.success_message), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.success_message), \
            "Success message was present, but now it is not"
