import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--language", action="store")


@pytest.fixture()
def language(request):
    return request.config.getoption("--language")
