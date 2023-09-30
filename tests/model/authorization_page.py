from selene import browser, have


class AuthorizationPage:

    def open_on_desktop(self):
        browser.open('')
        browser.element('[class*=sign-in]').click()

    def open_on_mobile(self):
        browser.open('')
        browser.element('.HeaderMenu-toggle-bar').click()
        browser.element('[class*=sign-in]').click()
