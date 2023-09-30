import pytest
from selene.support.shared import browser


@pytest.fixture(autouse=True)
def url():
    browser.config.base_url = "https://github.com"


"""Fixtures for test_fixtures"""


@pytest.fixture()
def window_size_desktop():
    browser.config.window_width = 1400
    browser.config.window_height = 1600


@pytest.fixture()
def window_size_mobile():
    browser.config.window_width = 390
    browser.config.window_height = 844


"""Fixture for test_parametrize"""


@pytest.fixture(params=['desktop', 'mobile'])
def set_window_size(request):
    if request.param == 'desktop':
        browser.config.window_width = 1400
        browser.config.window_height = 1600
    if request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844
