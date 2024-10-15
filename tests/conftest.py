import pytest
import allure
from extensions.functions import Functions
from flows.web_flows import WorkFlow
from helper.configuration_manager import BrowserManager
from helper.reporting_manager import ReportingManager
from pages.base_page import BasePage
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def setup_page(playwright: Playwright):
    browser, page = BrowserManager.setup(playwright)
    yield page
    browser.close()


@pytest.fixture(scope="function")
def initialize_pages(setup_page):
    pages = BasePage.initialize_all_pages(setup_page)
    BasePage.goto_homepage(pages)
    return pages

@pytest.fixture()
def add_allure_attach(request, setup_page):
    yield
    allure.attach(setup_page.screenshot(), name="After Test", attachment_type=allure.attachment_type.PNG)

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Send report after test execution"""
#     yield
#     if call.when == "teardown":
#         report_path = r'allure-report/index.html'
#         ReportingManager.send_report(report_path)
