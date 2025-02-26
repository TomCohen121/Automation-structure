import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.regular_loading #C20694
@allure.story("Delete Notebook Suspicious - Regular Loading")
@allure.description("Deleting the notebook's Suspicious using the 'Delete Notebook Check' button")
def test_regular_delete_notebook_suspicious(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(regular_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebookScreen
    f.functions.click_delete_notebook_if_enable()
    f.workflow.flow_set_suspicious_notebook()
    f.workflow.answer_one_question("1")
    f.functions.wait_for_element(f.checkNotebookPage.btn_delete_notebook_test())
    f.workflow.delete_notebook_test()
    f.workflow.assert_check_notebook_suspicious_deleted()
    f.checkNotebookPage.btn_x_suspicious_notebook_popup().click()
    f.breadcrumbs.btn_breadcrumbs_to_notebooks_page().click()

    #NotebookScreen
    f.functions.popup_answer_law()
    f.functions.assert_is_checkbox_checked(f.notebookPage.checkbox_notebook_suspicious_evaluation(2), expected_checked=False)
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    #PortionScreen
    table_num_of_suspicion_approved_after = f.functions.number_to_int(f.suspiciousLoadingPortionPage.txt_table_num_of_suspicion_approved(2))
    f.functions.assert_equal_to(table_num_of_suspicion_approved_after, 0,"Number of Suspicion Approved Notebooks is incorrect")

    soft_assert.assert_all()



