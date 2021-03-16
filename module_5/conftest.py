import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from stepik_lessons.module_5.pages.login_page import LoginPage
from stepik_lessons.module_5.pages.base_page import BasePage
from stepik_lessons.module_5.pages.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-GB")


@pytest.fixture()
def language(request):
    return request.config.getoption("--language")


@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': f"{language}, en"})
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def setup(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open(link)
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()
    login_page.register_new_user(BasePage.email, BasePage.password)
    login_page.should_be_authorized_user()
