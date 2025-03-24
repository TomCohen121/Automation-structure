import re
import time
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.mismatch_loading #C17638
@allure.story("Cancel Uncheck Portion - Mismatch Loading")
@allure.description("Cancel notebook UnCheck using the 'Cancel uncheck button")
def test_mismatch_cancel_notebook_uncheck(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(misMatch_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    #PortionScreen
    if f.portionPage.btn_approve_portion_uncheck().is_enabled():
        f.functions.click_button_if_enable(f.portionPage.btn_approve_portion_uncheck())
        f.functions.table_choose_a_row(2).dblclick()
    else:
        pass
    f.portionPage.btn_cancel_portion_uncheck().click()
    f.functions.table_choose_a_row(2).dblclick()
    checked_notebook_percent = f.portionPage.txt_table_percent_of_checked_notebooks(2)
    assert f.portionPage.txt_table_portion_status(2) == "מנה נשלחה לבדיקה"
    assert checked_notebook_percent == '0%'