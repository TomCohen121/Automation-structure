import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.senior_loading
@pytest.mark.senior_evaluator
@allure.story("E2E Test for Senior Loading - Senior Evaluator")
@allure.description("Notebook Checking and Loading Discharge Process")
def test_regular_loading_end_to_end(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(senior_loading_E2E_num,'senior_loading_E2E_num')
   #Dashboard
   # num_of_discharged_loadings_before = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_loadings())
   # num_of_discharged_portions_before = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_portions())
   # num_of_discharged_notebooks_before = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_notebooks())
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(senior_loading_E2E_num)
   f.functions.table_choose_a_row(2).click()
   stat_num_of_checked_portions_before = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_checked_portions())
   stat_num_of_unchecked_portions_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_num_of_unchecked_portions()))
   stat_num_of_checked_notebooks_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_checked_notebooks()))
   stat_num_of_unchecked_notebooks_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_unchecked_notebooks()))
   f.functions.table_choose_a_row(2).dblclick()

   #PortionScreen
   table_num_of_checked_notebooks_before = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))
   f.functions.table_choose_a_row(2).dblclick()

   #NotebookScreen
   f.functions.popup_answer_law()
   f.functions.table_choose_a_row(2).dblclick()

   #CheckNotebookScreen
   f.workflow.expert_notebook_checking_process()

   ##################################################################################################################################################################################
                                                                           # Testing
   #NotebookScreen
   f.functions.popup_answer_law()
   f.functions.assert_equal_to(f.notebookPage.txt_table_notebook_status(2),"מחברת נבדקה", "the Notebook status is not 'מחברת נבדקה'")
   f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

   #PortionScreen
   f.functions.assert_equal_to(f.portionPage.txt_table_portion_status(2),"מנה תקינה ממתינה למשיכת תפוקה","the Portion status is not 'מנה תקינה ממתינה למשיכת תפוקה'")
   table_num_of_checked_notebooks_after = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))
   f.functions.assert_equal_to(table_num_of_checked_notebooks_before+1,table_num_of_checked_notebooks_after,"Number of checked Notebooks is incorrect")
   f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

   #LoadingScreen
   stat_num_of_checked_portions_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_checked_portions())
   stat_num_of_unchecked_portions_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_num_of_unchecked_portions()))
   stat_num_of_checked_notebooks_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_checked_notebooks()))
   stat_num_of_unchecked_notebooks_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_unchecked_notebooks()))
   f.functions.assert_equal_to(stat_num_of_checked_portions_before +1, stat_num_of_checked_portions_after, "Statistics: Number of checked portions is incorrect")
   f.functions.assert_equal_to(stat_num_of_unchecked_portions_before -1, stat_num_of_unchecked_portions_after, "Statistics: Number of unchecked portions is incorrect")
   f.functions.assert_equal_to(stat_num_of_checked_notebooks_before +1, stat_num_of_checked_notebooks_after , "Statistics: Number of checked notebooks is incorrect")
   f.functions.assert_equal_to(stat_num_of_unchecked_notebooks_before -1, stat_num_of_unchecked_notebooks_after , "Statistics: Number of unchecked notebooks is incorrect")

   #ArchiveScreen
   # f.workflow.loading_discharge_and_navigate_to_archive()
   # f.functions.search_loading(senior_loading_E2E_num)
   # soft_assert.check(f.functions.table_choose_a_row(2).is_visible(),"The loading didn't appear in the archives")
   # f.breadcrumbs.btn_breadcrumbs_to_personal_area_page().click()

   #Dashboard
   # num_of_discharged_loadings_after = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_loadings())
   # num_of_discharged_portions_after = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_portions())
   # num_of_discharged_notebooks_after = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_notebooks())
   # f.functions.assert_equal_to(num_of_discharged_loadings_before+1 ,num_of_discharged_loadings_after , "Dashboard statistics: Number of discharged loadings is Incorrect")
   # f.functions.assert_equal_to(num_of_discharged_portions_before+1 ,num_of_discharged_portions_after , "Dashboard statistics: Number of discharged portions is Incorrect")
   # f.functions.assert_equal_to(num_of_discharged_notebooks_before+1 ,num_of_discharged_notebooks_after , "Dashboard statistics: Number of discharged notebooks is Incorrect")

   soft_assert.assert_all()