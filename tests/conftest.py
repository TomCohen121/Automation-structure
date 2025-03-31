import allure
import pytest
from playwright.sync_api import Playwright
from helper.configuration_manager import BrowserManager
from pages.base_page import BasePage

@pytest.fixture(scope="session")
def setup_page(playwright: Playwright):
    browser, page = BrowserManager.setup(playwright)
    yield page
    browser.close()

@pytest.fixture(scope="function")
def f(setup_page):
    base_page = BasePage(setup_page)  # Create an instance of BasePage
    base_page.initialize_all_pages()  # Initialize all pages
    BasePage.goto_homepage(base_page)  # Call the static method to navigate to the homepage
    return base_page  # Return the base_page instance to be used in tests

@pytest.fixture()
def add_allure_attach(request, setup_page):
    yield
    allure.attach(setup_page.screenshot(), name="After Test", attachment_type=allure.attachment_type.PNG)

