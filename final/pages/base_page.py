from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:
    base_url = "http://selenium1py.pythonanywhere.com/"
    login_page_link_locator = (By.ID, "login_link")
    view_basket_button_locator = (By.CSS_SELECTOR, "span.btn-group > a.btn-default")
    language_selector_locator = (By.CSS_SELECTOR, "select.form-control")
    confirm_language_change_button_locator = (By.XPATH, "//button[text()='Go']")

    def __init__(self, driver, url=base_url):
        self.driver = driver
        self.url = url

    def open(self, url=base_url, path=""):
        self.driver.get(url + path)

    def verify_url(self, path):
        url = self.driver.current_url
        assert path in url, \
            f"URL is not as expected.\n Current url: {url}, expected is {self.base_url + path}"

    def find_element_and_click_on_it(self, locator):
        web_element = self.driver.find_element(*locator)
        web_element.click()

    def find_text_input_and_complete_it(self, locator, value: str):
        text_input = self.driver.find_element(*locator)
        text_input.clear()
        text_input.send_keys(value)

    def open_login_page(self):
        self.find_element_and_click_on_it(self.login_page_link_locator)

    def open_basket_page(self):
        self.find_element_and_click_on_it(self.view_basket_button_locator)

    def verify_element_has_attribute(self, locator: tuple, attribute: str, attribute_value: str):
        web_element = self.driver.find_element(*locator)
        return attribute_value in web_element.get_attribute(attribute)

    def is_element_present(self, locator):
        if self.driver.find_element(*locator):
            return True

    def change_language(self, change_language):
        language_selector = Select(self.driver.find_element(*self.language_selector_locator))
        language_selector.select_by_value(change_language)
        self.find_element_and_click_on_it(self.confirm_language_change_button_locator)

    def verify_url_change_on_language_switch(self, new_language):
        return f"/{new_language}/" in self.driver.current_url
