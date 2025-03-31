import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *


@pytest.mark.regular_loading #C17638
@allure.story("Approve Uncheck Portion - Regular Loading")
@allure.description("Approve notebook UnCheck using the 'Approve uncheck' button")
def test_regular_approve_notebook_uncheck(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(regular_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    #PortionScreen
    f.functions.click_delete_portion_if_enabled()
    f.portionPage.btn_approve_portion_uncheck().click()
    f.functions.table_choose_a_row(2).dblclick()
    checked_notebook_percent = f.portionPage.txt_table_percent_of_checked_notebooks(2)
    assert checked_notebook_percent == '100%'
    assert f.portionPage.txt_table_portion_status(2) == "מנה סומנה כלא נבדקה"


