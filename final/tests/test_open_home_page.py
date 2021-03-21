from stepik_lessons.final.pages.home_page import HomePage


class TestOpenHomePage:
    def test_open_home_page(self, driver):
        home_page = HomePage(driver)

        home_page.open_home_page()
        home_page.verify_current_page_url()
