from selenium.webdriver.common.by import By

from final.pages.base_page import BasePage


class BasketPage(BasePage):
    """
    A class-container for Basket page. Is a child to BasePage.
    Contains page specific fields (data and locators) as well as methods.
    """
    basket_breadcrumb_locator = (By.XPATH, "//li[contains(text(), 'Basket')]")
    empty_basket_note_locator = (By.XPATH, "//p[normalize-space('Your Basket is empty.')]")
    breadcrumb_attribute = "class"
    breadcrumb_attribute_value = "active"

    def is_class_in_element(self):
        """
        Checks if web element has a specific class.
        (part of complex verification)
        """
        self.verify_element_has_attribute(self.basket_breadcrumb_locator, self.breadcrumb_attribute,
                                          self.breadcrumb_attribute_value)

    def is_empty_basket_note_present(self):
        """
        Checks if basket page has a note, meaning that basket is empty.
        (part of complex verification)
        """
        self.is_element_present(self.empty_basket_note_locator)

    def is_basket_empty(self):
        """
        Verifies if basket is empty.
        (complex verification, which consists of 2 methods)
        """
        self.is_class_in_element()
        self.is_empty_basket_note_present()
