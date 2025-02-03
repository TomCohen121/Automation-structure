import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.afterappeal_loading
@allure.story("E2E Test for AfterAppeal Loading")
@allure.description("AfterAppeal Notebook Checking and Loading Discharge Process")
def test_afterappeal_loading_end_to_end(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(appeal_loading_num, 'appeal_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()
   f.functions.search_loading(appeal_loading_num)

   #LoadingScreen
   f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

   #CheckNotebookScreen
   f.functions.click_delete_notebook_if_enable()
   f.workflow.notebook_checking_process_with_grade()

  ##################################################################################################################################################################################
                                                                           # Testing
   #NotebookScreen
   f.functions.popup_answer_law()
   table_num_of_checked_questions_after = f.functions.number_to_int(f.notebookPage.txt_table_num_of_checked_questions(2))
   table_notebook_grade_after = f.functions.number_to_int(f.notebookPage.txt_table_notebook_grade(2))
   f.functions.assert_equal_to(table_num_of_checked_questions_after,1, "Number of checked Questions is incorrect")
   f.functions.assert_equal_to(f.notebookPage.txt_table_notebook_status(2),"מחברת נבדקה", "the Notebook status is not 'מחברת נבדקה'")
   f.functions.assert_equal_to(table_notebook_grade_after,f.workflow.notebook_grade,"The Notebook grade is incorrect")
   f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

   #PortionScreen
   table_num_of_checked_notebooks_after = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))
   f.functions.assert_equal_to(table_num_of_checked_notebooks_after,1, "Number of checked Notebooks is incorrect")
   table_avg_grade_after = f.functions.number_to_int(f.portionPage.txt_table_avg_grade(2))
   f.functions.assert_equal_to(table_avg_grade_after,f.workflow.notebook_grade,"The Portion Average grade incorrect" )
   f.functions.assert_equal_to(f.portionPage.txt_table_portion_status(2),"מנה תקינה ממתינה למשיכת תפוקה","the Portion status is not 'מנה תקינה ממתינה למשיכת תפוקה'")
   f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

   #LoadingScreen
   stat_num_of_checked_portions_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_checked_portions())
   stat_num_of_unchecked_portions_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_num_of_unchecked_portions()))
   stat_num_of_checked_notebooks_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_checked_notebooks()))
   stat_num_of_unchecked_notebooks_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_unchecked_notebooks()))
   f.functions.assert_equal_to(stat_num_of_checked_portions_after,1, "Statistics: Number of checked portions is incorrect")
   f.functions.assert_equal_to(stat_num_of_unchecked_portions_after,0, "Statistics: Number of unchecked portions is incorrect")
   f.functions.assert_equal_to(stat_num_of_checked_notebooks_after,1, "Statistics: Number of checked notebooks is incorrect")
   f.functions.assert_equal_to(stat_num_of_unchecked_notebooks_after,0, "Statistics: Number of unchecked notebooks is incorrect")

   soft_assert.assert_all()
