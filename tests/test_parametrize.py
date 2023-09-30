"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, have


@pytest.mark.parametrize('set_window_size', ['desktop'], indirect=True)
def test_open_authorization_page_desktop(set_window_size):
    browser.open('')
    browser.element('[class*=sign-in]').click()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize('set_window_size', ['mobile'], indirect=True)
def test_open_authorization_page_mobile(set_window_size):
    browser.open('')
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('[class*=sign-in]').click()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))