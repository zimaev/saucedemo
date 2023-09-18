from playwright.sync_api import Page, expect

from components.login_form.login_form import LoginForm
from page_factory.title import Title
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.language_title = Title(
            page, locator="//div[@class='login_logo']", name='Swag Labs title'
        )
        self.login_form = LoginForm(page)

    def error_message_present(self):
        expect(self.login_form.error_msg).to_be_visible()
