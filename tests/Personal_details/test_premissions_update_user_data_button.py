import allure
import pytest
from pytest_playwright.pytest_playwright import page

@pytest.mark.permissions_update_user_data_button
@allure.story("Private distribution permissions for Profession")
@allure.description("Sending a message in Private distribution for Profession - Verifying message receipt")
def test_permissions_update_user_data_btn(f, add_allure_attach, page):
    f.personalDetailsPage.btn_personal_area_page_sidebar().click()
    f.functions.assert_element_exists(f.personalAreaPage.btn_view_update_user_data(),"The Component - צפייה ועדכון כל הנתונים")





