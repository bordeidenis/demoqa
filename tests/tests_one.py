from pages.base_page import BasePage


def test_open(open_browser_chrome):
    page = BasePage(open_browser_chrome, 'https://www.google.com')
    page.open()
