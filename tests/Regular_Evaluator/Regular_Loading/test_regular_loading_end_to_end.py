import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert


@pytest.mark.regular_evaluator
@allure.story("בדיקת E2E הערכה רגילה - מעריך רגיל")
@allure.description("תהליך בדיקת מחברת ופריקה של הטעינה")
def test_regular_loading_end_to_end(from_page, add_allure_attach, page):
   from_page["Functions"].wait_for_domcontentloaded()
   from_page["WorkFlow"].navigation_to_loading_screen()
   from_page["Functions"].search_loading(regular_loading_number)
   from_page["Functions"].table_choose_a_row(2).click()

   #LoadingScreen
   statistics_number_of_checked_portions_before = from_page["Functions"].extracting_value_from_statistics(from_page["LoadingPage"].txt_statistics_number_of_checked_portions())
   statistics_number_of_unchecked_portions_before = from_page["Functions"].extracting_value_from_statistics((from_page["LoadingPage"].txt_statistics_number_of_unchecked_portions()))
   statistics_number_of_checked_notebooks_before = from_page["Functions"].extracting_value_from_statistics((from_page["LoadingPage"].txt_statistics_checked_notebooks()))
   statistics_number_of_unchecked_notebooks_before = from_page["Functions"].extracting_value_from_statistics((from_page["LoadingPage"].txt_statistics_unchecked_notebooks()))

   from_page["Functions"].table_choose_a_row(2).dblclick()

   #PortionScreen
   from_page["Functions"].table_choose_a_row(2).click()
   table_number_of_checked_notebooks_before = from_page["PortionPage"].txt_table_number_of_checked_notebooks(2)
   table_avarage_grade_before = from_page["PortionPage"].txt_table_avg_grade(2)

   from_page["Functions"].table_choose_a_row(2).dblclick()

   #NotebookScreen
   from_page["Functions"].popup_answer_law()
   from_page["Functions"].table_choose_a_row(2).click()
   table_number_of_checked_questions_before = from_page["NotebookPage"].txt_table_number_of_checked_questions(2)
   table_notebook_grade_before = from_page["NotebookPage"].txt_table_notebook_grade(2)

   from_page["Functions"].table_choose_a_row(2).dblclick()

   #CheckNotebookScreen
   from_page["WorkFlow"].notebook_checking_process()
   from_page["Functions"].popup_answer_law()

# #################################################################################################################################################################################
                                                                           # Testing
    #NotebookScreen
   table_number_of_checked_questions_after = from_page["NotebookPage"].txt_table_number_of_checked_questions(2)
   from_page["Functions"].assert_equal_to(table_number_of_checked_questions_before+1,table_number_of_checked_questions_after,"Number of checked portions should be equal")
   from_page["Functions"].assert_equal_to(from_page["NotebookPage"].txt_table_notebook_status(2),"מחברת נבדקה", "the status is not 'מחברת שנבדקה'")
   from_page["Functions"].assert_equal_to(table_notebook_grade_before,from_page["WorkFlow"].notebook_grade,"The Notebook grade is not correct")

   from_page["Breadcrumbs"].btn_breadcrumbs_to_portions_page().click()

   #PortionScreen
   table_number_of_checked_notebooks_after = from_page["PortionPage"].txt_table_number_of_checked_notebooks(2)
   from_page["Functions"].assert_equal_to(table_number_of_checked_notebooks_before+1,table_number_of_checked_notebooks_after,"Number of checked portions should be equal")
   from_page["Functions"].assert_equal_to(table_avarage_grade_before,from_page["WorkFlow"].notebook_grade,"The average grade is not correct" )
   from_page["Functions"].assert_equal_to(from_page["PortionPage"].txt_table_portion_status(2),"מנה תקינה ממתינה למשיכת תפוקה","the status is not 'מנה תקינה ממתינה למשיכת תפוקה'")

   from_page["Breadcrumbs"].btn_breadcrumbs_to_loadings_page().click()

   #LoadingScreen
   statistics_number_of_checked_portions_after = from_page["Functions"].extracting_value_from_statistics(from_page["LoadingPage"].txt_statistics_number_of_checked_portions())
   statistics_number_of_unchecked_portions_after = from_page["Functions"].extracting_value_from_statistics((from_page["LoadingPage"].txt_statistics_number_of_unchecked_portions()))
   statistics_number_of_checked_notebooks_after = from_page["Functions"].extracting_value_from_statistics((from_page["LoadingPage"].txt_statistics_checked_notebooks()))
   statistics_number_of_unchecked_notebooks_after = from_page["Functions"].extracting_value_from_statistics((from_page["LoadingPage"].txt_statistics_unchecked_notebooks()))
   from_page["Functions"].assert_equal_to(statistics_number_of_checked_portions_before +1, statistics_number_of_checked_portions_after)
   from_page["Functions"].assert_equal_to(statistics_number_of_unchecked_portions_before +1, statistics_number_of_unchecked_portions_after)
   from_page["Functions"].assert_equal_to(statistics_number_of_checked_notebooks_before +1, statistics_number_of_checked_notebooks_after)
   from_page["Functions"].assert_equal_to(statistics_number_of_unchecked_notebooks_before +1, statistics_number_of_unchecked_notebooks_after)

   from_page["WorkFlow"].loading_discharge_and_navigate_to_archive()

   #ArchiveScreen
   from_page["Functions"].search_loading(regular_loading_number)
   soft_assert.check(from_page["Functions"].table_choose_a_row(2).is_visible(),"The loading didn't appear in the archives")
   soft_assert.assert_all()

