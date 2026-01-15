import pytest
from playwright.sync_api import sync_playwright
from utils import get_lambdatest_browser
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.fixture(params=["Chrome", "Safari"])
def browser_setup(request):
    browser_name = request.param

    with sync_playwright() as playwright:
        browser = get_lambdatest_browser(playwright, browser_name)
        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.fixture
def login_page(browser_setup):
    return LoginPage(browser_setup)


@pytest.fixture
def home_page(browser_setup):
    return HomePage(browser_setup)