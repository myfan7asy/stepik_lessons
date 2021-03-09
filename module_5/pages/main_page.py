from selenium.webdriver.common.by import By

from base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self, driver):
        link = self.driver.find_element_by_css_selector(By.CSS_SELECTOR, "#login_link")
        link.click()
