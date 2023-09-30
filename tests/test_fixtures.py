"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser, have


def test_authorization_desktop(window_size_desktop):
    browser.open('')
    browser.element('[class*=sign-in]').click()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))


def test_authorization_mobile(window_size_mobile):
    browser.open('')
    browser.element('.HeaderMenu-toggle-bar').click()
    browser.element('[class*=sign-in]').click()

    browser.element('.auth-form-header').should(have.exact_text('Sign in to GitHub'))
