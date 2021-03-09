link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    def test_guest_can_go_to_login_page(self, driver):
        driver.get(link)
        login_link = driver.find_element_by_css_selector("#login_link")
        login_link.click()
