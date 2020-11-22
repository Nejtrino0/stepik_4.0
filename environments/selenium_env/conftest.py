
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome")
    parser.addoption(
        "--language", action="store", default="en", help="my option: type1 or type2"
    )


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome")
    yield browser
    browser.quit()