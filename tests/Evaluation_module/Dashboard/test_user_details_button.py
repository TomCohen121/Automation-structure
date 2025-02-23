import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.senior_loading
@allure.story("Click on User Details Button")
@allure.description("Click on User Details Button - Navigate to user details page")
def test_user_details_button(f, add_allure_attach, page):
    #Dashboard
    with f.page.expect_navigation():
        f.personalAreaPage.btn_view_update_user_data().click()
    assert f.page.url.endswith("user-details"), f"Expected URL to end with 'user-details', but got: {page.url}"