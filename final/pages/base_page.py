from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:
    """
    A class-container for variables and methods. Includes all base methods/fields to be inherited by child classes.
    """
    base_url = "http://selenium1py.pythonanywhere.com/"
    login_page_link_locator = (By.ID, "login_link")
    view_basket_button_locator = (By.CSS_SELECTOR, "span.btn-group > a.btn-default")
    language_selector_locator = (By.CSS_SELECTOR, "select.form-control")
    confirm_language_change_button_locator = (By.XPATH, "//button[text()='Go']")
    search_input_locator = (By.ID, "id_q")
    search_submit_button_locator = (By.XPATH, "//input[@value='Search']")
    account_link_locator = (By.XPATH, "//a[@href='/en-gb/accounts/']")
    logout_link_locator = (By.ID, "logout_link")

    def __init__(self, driver, url=base_url):
        self.driver = driver
        self.url = url

    def open(self, url: str = base_url, path: str = None):
        """
        Open page as per URL and URL_path passed. In case if path is not passed - the only 'url' is opened.
        If path is in place, a combination of 'url' + 'path' will be opened.
        :url (str) - link we are about to visit. Takes 'base_url' value by default
        :path (str) - link path, adjustment to base url part. Takes 'None' value by default
        """
        if path is not None:
            self.driver.get(url + path)
        else:
            self.driver.get(url)

    def verify_url(self, path: str):
        """
        Verifies url of the current page.
        :url (str) - current webpage url address
        """
        url = self.driver.current_url
        assert path in url, \
            f"URL is not as expected.\n Current url: {url}, expected is {self.base_url + path}"

    def find_element_and_click_on_it(self, locator: tuple):
        """
        Looks for a web element and clicks on it.
        :locator (tuple) - should contain locator path and the way we look for it (ID, XPATH, CSS SELECTOR etc)
        """
        web_element = self.driver.find_element(*locator)
        web_element.click()

    def find_text_input_and_complete_it(self, locator: tuple, value: str):
        """
        Looks for a web element - input, clears is and completes with some value
        :locator (tuple) - should contain locator path and the way we look for it (ID, XPATH, CSS SELECTOR etc)
        :value (str) - something we are about to complete our input with
        (in most cases - 'str' is expected, but accepts int/float as well)
        """
        text_input = self.driver.find_element(*locator)
        text_input.clear()
        text_input.send_keys(value)

    def open_login_page(self):
        """
        A method to open login page by clicking on Login link.
        """
        self.find_element_and_click_on_it(self.login_page_link_locator)

    def open_basket_page(self):
        """
        A method to open basket page by clicking on Basket icon.
        """
        self.find_element_and_click_on_it(self.view_basket_button_locator)

    def verify_element_has_attribute(self, locator: tuple, attribute: str, attribute_value: str):
        """
        A method to verify if a specific web element has an attribute with a concrete value.
        :locator (tuple) - should contain locator path and the way we look for it (ID, XPATH, CSS SELECTOR etc)
        :attribute (str) - tag attribute we would like to verify
        :attribute_value (str) - attribute's specific value
        Return (bool) - 'True' of 'False' depending on method processing results
        """
        web_element = self.driver.find_element(*locator)
        return attribute_value in web_element.get_attribute(attribute)

    def is_element_present(self, locator: tuple):
        """
        A method to check if a specific web element is present on the page.
        :locator (tuple) - should contain locator path and the way we look for it (ID, XPATH, CSS SELECTOR etc)
        Return (bool) - 'True' if element is present
        """
        if self.driver.find_element(*locator):
            return True

    def is_element_not_present(self, locator: tuple):
        """
        A method to check if a specific web element is NOT present on the page.
        In case if element is not found, we seek for an 'NoSuchElementException' which is an expected result for us.
        :locator (tuple) - should contain locator path and the way we look for it (ID, XPATH, CSS SELECTOR etc)
        Return (bool) - 'True' if exception is caught
        """
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return True
        return False

    def change_language(self, new_language: str):
        """
        A method which interacts with language selector - selects a specific value from the select input.
        :new_language (str) - ISO code of a newly language value
        """
        language_selector = Select(self.driver.find_element(*self.language_selector_locator))
        language_selector.select_by_value(new_language)
        self.find_element_and_click_on_it(self.confirm_language_change_button_locator)

    def verify_url_change_on_language_switch(self, new_language: str):
        """
        Verifies that url is successfully updated as per language change. Url should contain ISO code of a newly
        selected language.
        :new_language (str) - ISO code of a newly language value
        Return (bool) - 'True' if url has language ISO code
        """
        return f"/{new_language}/" in self.driver.current_url

    def search_for_a_product(self, search_phrase: str):
        """
        Searches for a specific product, by completing Search input and submitting search.
        :search_phrase (str) - search keyword we are about to look for
        """
        self.find_text_input_and_complete_it(self.search_input_locator, search_phrase)
        self.find_element_and_click_on_it(self.search_submit_button_locator)

    def click_logout(self):
        """
        Clicks Logout link
        """
        self.find_element_and_click_on_it(self.logout_link_locator)

    def verify_successful_logout(self):
        """
        Verifies successful logout by checking absence of specific web elements.
        (complex verification, which consists of 2 methods)
        """
        self.verify_logout_link_absence()
        self.verify_account_link_absence()

    def verify_logout_link_absence(self):
        """
        Verifies successful logout by checking absence of Logout link.
        (part of complex verification)
        """
        self.is_element_not_present(self.logout_link_locator)

    def verify_account_link_absence(self):
        """
        Verifies successful logout by checking absence of Account link.
        (part of complex verification)
        """
        self.is_element_not_present(self.account_link_locator)
