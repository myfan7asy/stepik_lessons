from selenium.webdriver.common.by import By

from final.helpers.raw_data import locales
from final.pages.base_page import BasePage


class ProductPage(BasePage):
    """
    A class-container for Product page. Is a child to BasePage.
    Contains page specific fields (data and locators) as well as methods.
    """
    add_to_basket_button_locator = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    def verify_button_translation_change_on_language_switch(self, new_language: str):
        """
        Verifies if web site translations are affected according to language change.
        There is a dictionary ('locales') containing available languages and related button translations.
        Verification is considered as correct, if button translation corresponds to language selected.
        :new_language (str) - ISO code of a newly language value
        """
        add_to_cart_button = self.driver.find_element(*self.add_to_basket_button_locator)
        add_to_basket_text = add_to_cart_button.text
        assert add_to_basket_text == locales[f"{new_language}"], \
            f"Button text is not as expected. Actual: {add_to_basket_text}, expected is {locales[f'{new_language}']}"
