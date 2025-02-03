import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage


@pytest.mark.mismatch_loading
@allure.story("Set Suspicious Notebook Test for MisMatch Loading")
@allure.description("Set Suspicious Notebook Process and Loading Discharge For Mismatch Notebook")
def test_mismatch_loading_set_suspicious_notebook(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(misMatch_loading_num, 'misMatch_loading_num')
    # Dashboard
    f.workflow.navigation_to_loading_screen()
    f.functions.search_loading(misMatch_loading_num)

    # LoadingScreen
    f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

    #CheckNotebookScreen
    f.functions.click_delete_notebook_if_enable()
    f.workflow.flow_set_suspicious_notebook()
    f.workflow.mismatch_notebook_checking_process()

    #################################################################################################################################################
                                                                #Testing
    #NotebookScreen
    f.functions.popup_answer_law()
    f.functions.is_checkbox_checked(f.notebookPage.checkbox_notebook_suspicious_evaluation(2),expected_state=True,error_message="The Suspicious Evaluation Check box should be Marked")
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    #PortionScreen
    table_num_of_notebooks_in_suspicious_after = f.functions.number_to_int(f.portionPage.txt_table_num_of_suspicious_notebooks(2))
    f.functions.assert_equal_to(table_num_of_notebooks_in_suspicious_after,1, "Number of notebooks in Suspicious is incorrect")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

    #LoadingScreen
    stat_num_of_suspicious_notebooks_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_suspicious_notebooks())
    f.functions.assert_equal_to(stat_num_of_suspicious_notebooks_after,1, "Statistics: Number of Suspicious notebooks is incorrect")

    soft_assert.assert_all()


