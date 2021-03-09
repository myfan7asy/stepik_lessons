from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.driver.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()
