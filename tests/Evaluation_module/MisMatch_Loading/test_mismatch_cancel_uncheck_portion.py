import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *


@pytest.mark.mismatch_loading #C17638
@allure.story("Cancel Uncheck Portion - Mismatch Loading")
@allure.description("Cancel notebook UnCheck using the 'Cancel uncheck button")
def test_mismatch_cancel_notebook_uncheck(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(misMatch_loading_num, 'misMatch_loading_num')
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(misMatch_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    #PortionScreen
    if f.portionPage.btn_approve_portion_uncheck().is_enabled():
        f.functions.click_button_if_enabled(f.portionPage.btn_approve_portion_uncheck())
    else:
        pass
    f.portionPage.btn_cancel_portion_uncheck().click()
    f.functions.reload_page()
    checked_notebook_percent = f.portionPage.txt_table_percent_of_checked_notebooks(2)
    assert f.portionPage.txt_table_portion_status(2) == "מנה נשלחה לבדיקה"
    assert checked_notebook_percent == '0%'