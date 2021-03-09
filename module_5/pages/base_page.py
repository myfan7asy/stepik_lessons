from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver, link, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.link = link

    def open(self, link):
        self.driver.get(link)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_expected_url_opened(self, substring):
        if substring not in self.driver.current_url:
            return False
        return True
