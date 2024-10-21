import allure
import pytest
from allure_pytest.utils import allure_suite_labels
from pytest_playwright.pytest_playwright import page
from extensions.functions import Functions
from pages.base_page import BasePage
from helper.utils import loading_number
from soft_assert import soft_assert



@pytest.mark.marih
@allure.story("בדיקת E2E הערכה רגילה")
@allure.description("בדיקת1")
def test_regular_loading(from_page, add_allure_attach, page):
   from_page["Functions"].wait_for_domcontentloaded()
   from_page["WorkFlow"].navigation_to_loading_screen()
   from_page["Functions"].search_loading(loading_number)
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
   from_page["Functions"].assert_equal_to(table_number_of_checked_questions_before+1,table_number_of_checked_questions_after)
   from_page["Functions"].assert_equal_to(from_page["NotebookPage"].txt_table_notebook_status(2),"מחברת נבדקה")
   from_page["Functions"].assert_equal_to(table_notebook_grade_before,from_page["WorkFlow"].notebook_grade)

   from_page["NotebookPage"].btn_breadcrumbs_to_portions_page().click()

   #PortionScreen
   table_number_of_checked_notebooks_after = from_page["PortionPage"].txt_table_number_of_checked_notebooks(2)
   from_page["Functions"].assert_equal_to(table_number_of_checked_notebooks_before+1,table_number_of_checked_notebooks_after)
   from_page["Functions"].assert_equal_to(table_avarage_grade_before,from_page["WorkFlow"].notebook_grade)
   from_page["Functions"].assert_equal_to(from_page["PortionPage"].txt_table_portion_status(2),"מנה תקינה ממתינה למשיכת תפוקה")

   from_page["PortionPage"].btn_breadcrumbs_to_loadings_page().click()

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
   from_page["Functions"].search_loading(loading_number)
   soft_assert.check(from_page["Functions"].table_choose_a_row(2).is_visible())
   soft_assert.assert_all()

