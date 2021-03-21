class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url: str):
        self.driver.get(url)

    def get_page_url(self):
        return self.driver.current_url

    def find_element_and_click_on_it(self, locator):
        web_element = self.driver.find_element(*locator)
        web_element.click()

    def find_text_input_clear_and_complete_it(self, locator, value: str):
        text_input = self.driver.find_element(*locator)
        text_input.clear()
        text_input.send_keys(value)
