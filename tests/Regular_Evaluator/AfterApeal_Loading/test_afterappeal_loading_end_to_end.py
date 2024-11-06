import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.afterappeal_loading
@pytest.mark.regular_evaluator
@allure.story("E2E Test for AfterAppeal Loading - Regular Evaluator")
@allure.description("Notebook Checking and Loading Discharge Process")
def test_afterappeal_loading_end_to_end(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(after_appeal_loading_number_E2E,'after_appeal_loading_number_E2E')
   #Dashboard
   # num_of_discharged_loadings_before = f.functions.number_to_int(f.personal_areaPage.txt_num_of_discharged_loadings())
   # num_of_discharged_portions_before = f.functions.number_to_int(f.personal_areaPage.txt_num_of_discharged_portions())
   # num_of_discharged_notebooks_before = f.functions.number_to_int(f.personal_areaPage.txt_num_of_discharged_notebooks())

   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(after_appeal_loading_number_E2E)
   f.functions.table_choose_a_row(2).click()
   stat_num_of_checked_portions_before = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_checked_portions())
   stat_num_of_unchecked_portions_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_num_of_unchecked_portions()))
   stat_num_of_checked_notebooks_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_checked_notebooks()))
   stat_num_of_unchecked_notebooks_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_unchecked_notebooks()))
   f.functions.table_choose_a_row(2).dblclick()

   #PortionScreen
   f.functions.table_choose_a_row(2).click()
   table_num_of_checked_notebooks_before = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))

   f.functions.table_choose_a_row(2).dblclick()

   #NotebookScreen
   f.functions.popup_answer_law()
   f.functions.table_choose_a_row(2).click()
   table_num_of_checked_questions_before = f.functions.number_to_int(f.notebookPage.txt_table_num_of_checked_questions(2))

   f.functions.table_choose_a_row(2).dblclick()

   #CheckNotebookScreen
   f.workflow.notebook_checking_process_with_grade()
   f.functions.popup_answer_law()

  ##################################################################################################################################################################################
                                                                           # Testing
   #NotebookScreen
   table_num_of_checked_questions_after = f.functions.number_to_int(f.notebookPage.txt_table_num_of_checked_questions(2))
   table_notebook_grade_after = f.functions.number_to_int(f.notebookPage.txt_table_notebook_grade(2))
   f.functions.assert_equal_to(table_num_of_checked_questions_before+1,table_num_of_checked_questions_after,"Number of checked Questions is incorrect")
   f.functions.assert_equal_to(f.notebookPage.txt_table_notebook_status(2),"מחברת נבדקה", "the status is not 'מחברת נבדקה'")
   f.functions.assert_equal_to(table_notebook_grade_after,f.workflow.notebook_grade,"The Notebook grade is incorrect")

   f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

   #PortionScreen
   table_num_of_checked_notebooks_after = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))
   f.functions.assert_equal_to(table_num_of_checked_notebooks_before+1,table_num_of_checked_notebooks_after,"Number of checked Notebooks is incorrect")
   table_avg_grade_after = f.functions.number_to_int(f.portionPage.txt_table_avg_grade(2))
   f.functions.assert_equal_to(table_avg_grade_after,f.workflow.notebook_grade,"The Portion Average grade incorrect" )
   f.functions.assert_equal_to(f.portionPage.txt_table_portion_status(2),"מנה תקינה ממתינה למשיכת תפוקה","the status is not 'מנה תקינה ממתינה למשיכת תפוקה'")

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

   # f.workflow.loading_discharge_and_navigate_to_archive()

   # #ArchiveScreen
   # f.functions.search_loading(regular_loading_number_E2E)
   # soft_assert.check(f.functions.table_choose_a_row(2).is_visible(),"The loading didn't appear in the archives")

   #Dashboard
   # f.breadcrumbs.btn_breadcrumbs_to_personal_area_page().click()
   # num_of_discharged_loadings_after = f.functions.number_to_int(f.personal_areaPage.txt_num_of_discharged_loadings())
   # num_of_discharged_portions_after = f.functions.number_to_int(f.personal_areaPage.txt_num_of_discharged_portions())
   # num_of_discharged_notebooks_after = f.functions.number_to_int(f.personal_areaPage.txt_num_of_discharged_notebooks())

   # f.functions.assert_equal_to(num_of_discharged_loadings_before+1 ,num_of_discharged_loadings_after , "Dashboard statistics: Number of discharged loadings is Incorrect")
   # f.functions.assert_equal_to(num_of_discharged_portions_before+1 ,num_of_discharged_portions_after , "Dashboard statistics: Number of discharged portions is Incorrect")
   # f.functions.assert_equal_to(num_of_discharged_notebooks_before+1 ,num_of_discharged_notebooks_after , "Dashboard statistics: Number of discharged notebooks is Incorrect")

   soft_assert.assert_all()
