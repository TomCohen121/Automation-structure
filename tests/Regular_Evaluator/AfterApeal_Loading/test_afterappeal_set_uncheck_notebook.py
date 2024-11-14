import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage


@pytest.mark.afterappeal_loading
@pytest.mark.regular_evaluator
@allure.story("Set Uncheck Notebook Test for AfterAppel Loading - Regular Evaluator")
@allure.description("Set Uncheck Notebook Process and Loading Discharge")
def test_afterappeal_loading_set_uncheck_notebook(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(appeal_loading_set_unchecked_num, 'appeal_loading_set_unchecked_num')
    f.functions.wait_for_networkidle()

    #Dashboard
    num_of_uncheck_notebooks_before = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_uncheck_notebooks())
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(appeal_loading_set_unchecked_num)
    f.functions.table_choose_a_row(2).click()
    stat_num_of_nocheck_portions_before = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_nocheck_portions())
    stat_num_of_nocheck_notebooks_before = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_nocheck_notebooks())
    f.functions.table_choose_a_row(2).dblclick()

    #PortionScreen
    table_num_of_checked_notebooks_before = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))
    f.functions.table_choose_a_row(2).dblclick()

    #NotebookScreen
    f.functions.popup_answer_law()
    f.functions.table_choose_a_row(2).dblclick()

    #CheckNotebookScreen
    f.workflow.flow_set_uncheck_notebook()

    ######################################################################################################################################################
                                                                # Testing
    #NotebookScreen
    f.functions.popup_answer_law()
    notebook_status = f.notebookPage.txt_table_notebook_status(2).strip()
    f.functions.assert_equal_to(notebook_status,f.workflow.uncheck_reason,"The Notebook Status is not equal to the Uncheck reason")
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    #PortionScreen
    table_num_of_checked_notebooks_after = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))
    f.functions.assert_equal_to(table_num_of_checked_notebooks_before + 1, table_num_of_checked_notebooks_after,"Number of checked Notebooks is incorrect")
    f.functions.assert_equal_to(f.portionPage.txt_table_portion_status(2), "מנה עם שאלון לא מתאים","the Portion status is not 'מנה עם שאלון לא מתאים'")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

    #LoadingScreen
    stat_num_of_nocheck_portions_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_nocheck_portions())
    stat_num_of_nocheck_notebooks_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_nocheck_notebooks())
    f.functions.assert_equal_to(stat_num_of_nocheck_notebooks_before+1,stat_num_of_nocheck_notebooks_after, "Statistics: Number of uncheck portions is incorrect")
    f.functions.assert_equal_to(stat_num_of_nocheck_portions_before+1,stat_num_of_nocheck_portions_after, "Statistics: Number of uncheck notebooks is incorrect")

    #ArchiveScreen
    # f.workflow.loading_discharge_and_navigate_to_archive()
    # f.functions.search_loading(appeal_loading_set_unchecked_num)
    # soft_assert.check(f.functions.table_choose_a_row(2).is_visible(),"The loading didn't appear in the archives")
    f.breadcrumbs.btn_breadcrumbs_to_personal_area_page().click()

    #Dashboard
    num_of_uncheck_notebooks_after = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_uncheck_notebooks())
    f.functions.assert_equal_to(num_of_uncheck_notebooks_before+1 ,num_of_uncheck_notebooks_after , "Dashboard statistics: Number of discharged notebooks is Incorrect")

    soft_assert.assert_all()

