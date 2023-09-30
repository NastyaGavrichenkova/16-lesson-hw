"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have
from tests.model.authorization_page import AuthorizationPage

authorization_page = AuthorizationPage()


def test_open_authorization_page_desktop(set_window_size):
    if browser.config.window_width <= 390:
        pytest.skip("It's mobile aspect ratio")

    authorization_page.open_on_desktop()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_open_authorization_page_mobile(set_window_size):
    if browser.config.window_width > 390:
        pytest.skip("It's desktop aspect ratio")

    authorization_page.open_on_mobile()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))