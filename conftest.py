import pytest
from playwright.sync_api import Browser, Page


@pytest.fixture(scope="session")
def browser_page(browser: Browser):
    new_page = browser.new_page()
    yield new_page
    new_page.close()


@pytest.fixture(scope="session", autouse=True)
def open_to_url(browser_page: Page, base_url):
    browser_page.goto('https://www.knowtheromans.com/roman-numerals/')
    return browser_page