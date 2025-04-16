import allure
import pytest
from pytest_playwright.pytest_playwright import page


@allure.story("Private distribution permissions for Profession")
@allure.description("Sending a message in Private distribution for Profession - Verifying message receipt")
def test_update_examiner_phone(f, add_allure_attach, page):
    f.personalAreaPage.btn_view_update_user_data().click()
    f.personalDetailsPage.rol_examiner_phone().click()
    f.personalDetailsPage.btn_update_examiner_phone().click()
    f.personalDetailsPage.btn_add_new_examiner_phone().click()
    f.personalDetailsPage.field_examiner_phone().fill("3897241")
    f.personalDetailsPage.field_examiner_area_code().fill("052")
    f.personalDetailsPage.btn_save_new_phone().click()
