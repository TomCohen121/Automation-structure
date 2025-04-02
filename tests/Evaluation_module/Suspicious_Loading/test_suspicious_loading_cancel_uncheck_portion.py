import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *


@pytest.mark.suspicious_loading #C17638
@allure.story("Cancel Uncheck Portion - Suspicious Loading")
@allure.description("Cancel notebook UnCheck using the 'Cancel uncheck button")
def test_suspicious_cancel_notebook_uncheck(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(suspicious_loading_num, 'suspicious_loading_num')
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(suspicious_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    #PortionScreen
    f.functions.click_delete_portion_if_enabled()
    f.portionPage.btn_approve_portion_uncheck().click()
    f.portionPage.btn_cancel_portion_uncheck().click()
    f.functions.reload_page()
    assert f.portionPage.txt_table_portion_status(2) == "מנה נשלחה לבדיקה"
