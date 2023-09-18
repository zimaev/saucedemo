import pytest

from pages.playwright_home_page import PlaywrightHomePage
from pages.playwright_languages_page import PlaywrightLanguagesPage
from settings import BASE_URL


class TestSearch:
    @pytest.mark.parametrize('keyword', ['python'])
    def test_search(self, keyword: str, playwright_home_page, playwright_languages_page):
        playwright_home_page.visit(BASE_URL)
        playwright_home_page.navbar.open_search()
        playwright_home_page.navbar.search_modal.find_result(
            keyword, result_number=0
        )

        playwright_languages_page.language_present(language=keyword)


class TestLogin:
    @pytest.mark.parametrize('username, password', [("standard_user", "secret_sauce"),
                                                    ("problem_user", "secret_sauce"),
                                                    ("performance_glitch_user", "secret_sauce")])
    def test_valid_login(self, login_page, username, password):
        login_page.visit(BASE_URL)
        login_page.login_form.fill_username_input(username)
        login_page.login_form.fill_password_input(password)
        login_page.login_form.click_login_button()

    def test_failed_login(self):
        pass
