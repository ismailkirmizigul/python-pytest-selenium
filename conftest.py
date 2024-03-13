import json

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.HomePage import HomePage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


@pytest.fixture(scope="session")
def config():
    BROWSERS = ['Chrome', 'Firefox']

    with open('config.json') as config_file:
        config_data = json.load(config_file)

    browser = config_data.get('browser')
    headless = config_data.get('headless')
    implicit_wait = config_data.get('implicit_wait')

    assert browser in BROWSERS
    assert isinstance(headless, bool)
    assert isinstance(implicit_wait, int)
    assert implicit_wait > 0

    return {
        'browser': browser,
        'headless': headless,
        'implicit_wait': implicit_wait
    }


@pytest.fixture(scope="module")
def browser(config):
    if config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        if config['headless']:
            opts.add_argument('headless')
        b = webdriver.Chrome(options=opts)
    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        if config['headless']:
            opts.headless = True
        b = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    b.implicitly_wait(config['implicit_wait'])

    yield b

    b.quit()

def openWebPage(browser):
    browser.get("https://useinsider.com")
    browser.maximize_window()

    HomePage(browser).clickAcceptAllCookies()