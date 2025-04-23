import allure
import pytest
from pytest_playwright.pytest_playwright import page

@pytest.mark.permissions_personal_area_button
@allure.story("Private distribution permissions for Profession")
@allure.description("Sending a message in Private distribution for Profession - Verifying message receipt")
def test_permissions_personal_area_btn(f, add_allure_attach, page):
    f.functions.assert_element_exists(f.personalDetailsPage.btn_personal_area_page_sidebar(),"The Component - איזור אישי")