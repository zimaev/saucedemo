import logging

import allure
from playwright.sync_api import Page, Response
from helper.log import logger
from components.navigation.navbar import Navbar


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.logger = logger
        self.navbar = Navbar(page)

    def visit(self, url: str) -> Response | None:
        with allure.step(f'Opening the url "{url}"'):
            self.logger.info(f'Opening the url "{url}"')
            return self.page.goto(url, wait_until='networkidle')

    def reload(self) -> Response | None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')



