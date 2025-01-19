import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage

@pytest.mark.senior_loading
@allure.story("Set Suspicious Notebook Test for Senior Loading")
@allure.description("Set Suspicious Notebook Process and Loading Discharge For Senior Notebook")
def test_senior_loading_set_suspicious_notebook(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(senior_loading_set_suspicious_num, 'senior_loading_set_suspicious_num')
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(senior_loading_set_suspicious_num)
    f.functions.table_choose_a_row(2).click()
    stat_num_of_suspicious_notebooks_before = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_suspicious_notebooks())
    f.functions.table_choose_a_row(2).dblclick()

    #PortionScreen
    table_num_of_notebooks_in_suspicious_before = f.functions.number_to_int(f.portionPage.txt_table_num_of_suspicious_notebooks(2))
    f.functions.table_choose_a_row(2).dblclick()

    #NotebookScreen
    f.functions.popup_answer_law()
    f.functions.table_choose_a_row(2).dblclick()

    #CheckNotebookScreen
    f.workflow.flow_set_suspicious_notebook()
    f.workflow.senior_notebook_checking_process()

    #################################################################################################################################################
                                                                #Testing
    #NotebookScreen
    f.functions.popup_answer_law()
    f.functions.is_checkbox_checked(f.notebookPage.checkbox_notebook_suspicious_evaluation(2),expected_state=True,error_message="The Suspicious Evaluation Check box should be Marked")
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    #PortionScreen
    table_num_of_notebooks_in_suspicious_after = f.functions.number_to_int(f.portionPage.txt_table_num_of_suspicious_notebooks(2))
    f.functions.assert_equal_to(table_num_of_notebooks_in_suspicious_before+1,table_num_of_notebooks_in_suspicious_after , "Number of notebooks in Suspicious is incorrect")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

    #LoadingScreen
    stat_num_of_suspicious_notebooks_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_suspicious_notebooks())
    f.functions.assert_equal_to(stat_num_of_suspicious_notebooks_before+1,stat_num_of_suspicious_notebooks_after, "Statistics: Number of Suspicious notebooks is incorrect")

    # #ArchiveScreen
    # f.workflow.loading_discharge_and_navigate_to_archive()
    # f.functions.search_loading(senior_loading_set_suspicious_num)
    # f.functions.reload_page()
    # f.functions.assert_element_exists(f.functions.table_choose_a_row(2),"The loading didn't appear in the archives")

    soft_assert.assert_all()


