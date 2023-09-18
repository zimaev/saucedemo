import pytest
from playwright.sync_api import Page, sync_playwright
import logging

from pages.playwright_home_page import PlaywrightHomePage
from pages.playwright_languages_page import PlaywrightLanguagesPage
from pages.login_page import LoginPage


@pytest.fixture(scope='function')
def playwright_home_page(page) -> PlaywrightHomePage:
    return PlaywrightHomePage(page)


@pytest.fixture(scope='function')
def playwright_languages_page(page) -> PlaywrightLanguagesPage:
    return PlaywrightLanguagesPage(page)


@pytest.fixture()
def login_page(page):
    return LoginPage(page)
