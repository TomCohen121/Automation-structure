import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.suspiciuous_loading
@allure.story("Delete Portion Data - Suspicious Loading")
@allure.description("Deleting the Portion Data using the 'Delete Portion data' button")
def test_suspicious_delete_portion_data(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(suspicious_loading_num, 'suspicious_loading_num')
    # Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(suspicious_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebookScreen
    f.functions.click_delete_notebook_if_enable_suspicious()
    f.workflow.notebook_suspicion_approved_process()

    ##################################################################################################################################################################################
                                                                 # Testing
    # NotebookScreen
    f.functions.popup_answer_law()
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()
    f.portionPage.btn_delete_portion_data().click()
    f.portionPage.btn_save_delete_portion_data().click()
    table_num_of_suspicion_approved_after = f.functions.number_to_int(f.suspiciousLoadingPortionPage.txt_table_num_of_suspicion_approved(2))
    f.functions.assert_equal_to(table_num_of_suspicion_approved_after, 0,"Number of Suspicion Approved Notebooks is incorrect")
    f.functions.assert_equal_to(f.portionPage.txt_table_portion_status(2), "מנה נשלחה לבדיקה","the Portion status is not 'מנה נשלחה לבדיקה'")




