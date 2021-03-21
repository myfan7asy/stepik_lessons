from selenium.webdriver.common.by import By

from helpers.locales import locales
from pages.base_page import BasePage


class ProductPage(BasePage):
    add_to_basket_button_locator = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    def verify_button_translation_change_on_language_switch(self, new_language):
        add_to_cart_button = self.driver.find_element(*self.add_to_basket_button_locator)
        add_to_basket_text = add_to_cart_button.text
        assert add_to_basket_text == locales[f"{new_language}"], \
            f"Button text is not as expected. Actual: {add_to_basket_text}, expected is {locales[f'{new_language}']}"
