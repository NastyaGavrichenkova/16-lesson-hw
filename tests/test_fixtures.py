"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser, have
from tests.model.authorization_page import AuthorizationPage

authorization_page = AuthorizationPage()


def test_open_authorization_page_desktop(window_size_desktop):
    authorization_page.open_on_desktop()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_open_authorization_page_mobile(window_size_mobile):
    authorization_page.open_on_mobile()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
