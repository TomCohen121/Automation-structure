import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *


@pytest.mark.afterappeal_loading #C17638
@allure.story("Cancel Uncheck Portion - AfterAppeal Loading")
@allure.description("Cancel notebook UnCheck using the 'Cancel uncheck button")
def test_afterappeal_cancel_notebook_uncheck(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(appeal_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    #PortionScreen
    f.functions.click_delete_portion_if_enabled()
    f.portionPage.btn_approve_portion_uncheck().click()
    f.functions.table_choose_a_row(2).dblclick()
    f.portionPage.btn_cancel_portion_uncheck().click()
    f.functions.table_choose_a_row(2).dblclick()
    checked_notebook_percent = f.portionPage.txt_table_percent_of_checked_notebooks(2)
    assert f.portionPage.txt_table_portion_status(2) == "מנה נשלחה לבדיקה"
    assert checked_notebook_percent == '0%'