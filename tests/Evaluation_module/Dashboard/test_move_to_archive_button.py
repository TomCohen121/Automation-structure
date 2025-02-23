import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.senior_loading
@allure.story("Click on Move to Archive Button")
@allure.description("Click on Move to Archive Button - navigate to user details page")
def test_move_to_archive_button(f, add_allure_attach, page):
    #Dashboard
    with f.page.expect_navigation():
        f.personalAreaPage.btn_move_to_archive().click()
    assert f.page.url.endswith("archived"), f"Expected URL to end with 'archived', but got: {page.url}"