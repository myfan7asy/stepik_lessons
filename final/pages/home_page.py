from stepik_lessons.final.pages.base_page import BasePage


class HomePage(BasePage):
    __home_page_url = "http://selenium1py.pythonanywhere.com/"

    def open_home_page(self):
        self.open_page(self.__home_page_url)

    def verify_current_page_url(self):
        current_page_url = self.get_page_url()
        assert current_page_url == self.__home_page_url, \
            f"Observed page has unexpected URL.\nActual: {self.driver.current_url}, expected is {self.__home_page_url}"
