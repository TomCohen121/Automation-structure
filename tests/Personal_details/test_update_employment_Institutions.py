import allure
import pytest
from pytest_playwright.pytest_playwright import page
from datetime import datetime


@allure.story("Private distribution permissions for Profession")
@allure.description("Sending a message in Private distribution for Profession - Verifying message receipt")
def test_update_employment_institutions(f, add_allure_attach, page):
    today = datetime.today()
    target_day = 1
    target_month = today.month
    target_year = today.year
    aria_label = f"{target_day}-{target_month}-{target_year}"

    f.personalAreaPage.btn_view_update_user_data().click()
    f.personalDetailsPage.btn_update_employment_institutions().click()
    f.personalDetailsPage.btn_add_new_row().click()
    f.page.locator('app-date-picker-input[ng-reflect-name="finishDate"] input[readonly]').nth(12).click()
    f.page.locator(f'div[role="gridcell"][aria-label="{aria_label}"]').click()
