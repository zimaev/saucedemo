from playwright.sync_api import Page

from page_factory.button import Button

from page_factory.component import Component
from page_factory.error_message import ErrorMessage
from page_factory.input import Input


class LoginForm:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.username_input = Input(page, "//input[@id='user-name']", "Username")
        self.password_input = Input(page, "//input[@id='password']", "Password")
        self.login_button = Button(page, "//input[@id='login-button']", "Login")
        self.error_msg = ErrorMessage(page, "//h3[@data-test='error']", "ErrorMessage")

    def fill_username_input(self, username):
        self.username_input.fill(username)

    def fill_password_input(self, password):
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()







