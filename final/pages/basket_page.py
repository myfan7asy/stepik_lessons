from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BasketPage(BasePage):
    basket_breadcrumb_locator = (By.XPATH, "//li[contains(text(), 'Basket')]")
    empty_basket_note_locator = (By.XPATH, "//p[normalize-space('Your Basket is empty.')]")
    breadcrumb_attribute = "class"
    breadcrumb_attribute_value = "active"

    def is_class_in_element(self):
        self.verify_element_has_attribute(self.basket_breadcrumb_locator, self.breadcrumb_attribute,
                                          self.breadcrumb_attribute_value)

    def is_empty_basket_note_present(self):
        self.is_element_present(self.empty_basket_note_locator)

    def is_basket_empty(self):
        self.is_class_in_element()
        self.is_empty_basket_note_present()
