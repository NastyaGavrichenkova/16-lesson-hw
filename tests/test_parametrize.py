"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have
from tests.model.authorization_page import AuthorizationPage

authorization_page = AuthorizationPage()


@pytest.mark.parametrize('set_window_size', ['desktop'], indirect=True)
def test_open_authorization_page_desktop(set_window_size):
    authorization_page.open_on_desktop()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize('set_window_size', ['mobile'], indirect=True)
def test_open_authorization_page_mobile(set_window_size):
    authorization_page.open_on_mobile()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))