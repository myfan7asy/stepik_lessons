from pages.product_page import ProductPage


class TestChangeLanguageFromAProductPage:
    language = "es"
    product_page_path = "catalogue/excession_51/"

    def test_switch_language_and_verify_changes(self, driver):
        product_page = ProductPage(driver)
        product_page.open(self.product_page_path)
        product_page.verify_url(self.product_page_path)
        product_page.change_language(self.language)
        product_page.verify_url_change_on_language_switch(self.language)
        product_page.verify_button_translation_change_on_language_switch(self.language)
