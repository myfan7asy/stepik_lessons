import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-GB",
                     help="Choose one of languages: ar, it, uk or en-GB")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose one of available browsers: chrome, firefox or chrome-headless")


@pytest.fixture()
def driver(request):
    language = request.config.getoption("language")
    browser = request.config.getoption("browser")

    chrome_options = webdriver.ChromeOptions()
    locale_option = ('prefs', {'intl.accept_languages': f"{language}, en"})

    if browser == "chrome":
        chrome_options.add_experimental_option(*locale_option)
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    elif browser == "chrome-headless":
        chrome_options.add_experimental_option(*locale_option)
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise pytest.UsageError("--browser should be chrome, firefox or chrome-headless")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()
