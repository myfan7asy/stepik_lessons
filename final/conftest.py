import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-GB")


@pytest.fixture()
def language(request):
    return request.config.getoption("--language")


@pytest.fixture()
def driver(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': f"{language}, en"})
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
