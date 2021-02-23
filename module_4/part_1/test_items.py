from helper import *


def test_open_url_and_verify_language(driver, language):
    if language in locales.keys():
        locale = locales[language][0]
        driver.get(f"http://selenium1py.pythonanywhere.com/{locale}/catalogue/coders-at-work_207/")
        button_value = locales[language][1]
        button = driver.find_element_by_css_selector(f"button[value='{button_value}']")
        assert button, "Button value does not match with language selected"
