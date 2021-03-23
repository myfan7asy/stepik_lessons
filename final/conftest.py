import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-GB",
                     help="Choose one of languages: ar, it, uk or en-GB")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose one of available browsers: chrome, chrome-headless, firefox")


def create_chrome(language, headless=False) -> webdriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': f"{language}, en"})
    if headless:
        chrome_options.add_argument("--headless")
    else:
        chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)


def create_firefox():
    return webdriver.Firefox(executable_path=GeckoDriverManager().install())


@pytest.fixture()
def driver(request):
    driver = None
    language = request.config.getoption("language")
    browser = request.config.getoption("browser")

    if browser == "chrome":
        driver = create_chrome(language)
    elif browser == "chrome-headless":
        driver = create_chrome(language, headless=True)
    elif browser == "firefox":
        driver = create_firefox()
    else:
        raise pytest.UsageError("--browsers: chrome, chrome-headless, firefox")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
