import allure
import pytest
from allure_pytest.utils import allure_suite_labels
from pytest_playwright.pytest_playwright import page
from pages.base_page import BasePage




@pytest.mark.marih
@allure.story("בדיקת E2E הערכה רגילה")
@allure.description("בדיקת1")
def test_regular_loading(from_page, add_allure_attach, page):
   from_page["WorkFlow"].navigation_to_loading_screen()
   from_page["Functions"].search_loading('0045564')
   from_page["Functions"].table_choose_a_row(2).click()

   #מסך טעינות
   statistics_number_of_checked_portions_before = from_page["Functions"].extracting_value_from_statistics(from_page["LoadingPage"].txt_statistics_number_of_checked_portions())

   statistics_number_of_unchecked_portions_before = from_page["Functions"].extracting_value_from_statistics((from_page["LoadingPage"].txt_statistics_number_of_unchecked_portions()))

   statistics_number_of_checked_notebooks_before = from_page["Functions"].extracting_value_from_statistics((from_page["LoadingPage"].txt_statistics_checked_notebooks()))

   statistics_number_of_unchecked_notebooks_before = from_page["Functions"].extracting_value_from_statistics((from_page["LoadingPage"].txt_statistics_unchecked_notebooks()))
   from_page["Functions"].table_choose_a_row(2).dblclick()

   #מסך מנות
   from_page["Functions"].table_choose_a_row(2).click()
   table_number_of_checked_notebooks_before = from_page["PortionPage"].txt_table_number_of_checked_notebooks(2)

   table_avarage_grade_before = from_page["PortionPage"].txt_table_avg_grade(2)

   from_page["Functions"].table_choose_a_row(2).dblclick()

   #מסך מחברות
   from_page["Functions"].popup_answer_law()
   from_page["Functions"].table_choose_a_row(2).click()

   table_number_of_checked_questions_before = from_page["NotebookPage"].txt_table_number_of_checked_questions(2)

   table_notebook_grade_before = from_page["NotebookPage"].txt_table_notebook_grade(2)

   from_page["Functions"].table_choose_a_row(2).dblclick()

   #מסך בדיקת מחברת
   from_page["WorkFlow"].notebook_checking_process()
   from_page["Functions"].popup_answer_law()
#
# ######################################################################
# #תחילת בדיקות
#    #מסך מחברות
#    table_number_of_checked_questions_after = from_page["NotebookPage"].txt_table_number_of_checked_questions(2)
#    from_page["Functions"].assert_equal_to(table_number_of_checked_questions_before+1,table_number_of_checked_questions_after)
#
#    from_page["Functions"].assert_equal_to(from_page["NotebookPage"].txt_table_notebook_status(2),"מחברת נבדקה")

   # from_page["NotebookPage"].btn_breadcrumbs_to_portions_page().click()
   # table_number_of_checked_notebooks_after = from_page["PortionPage"].txt_table_number_of_checked_notebooks(2)
   # assert table_number_of_checked_notebooks_before +1 == table_number_of_checked_notebooks_after

   # from_page["PortionPage"].btn_breadcrumbs_to_loadings_page().click()
   # statistics_number_of_checked_portions_after = from_page["Functions"].extracting_value_from_statistics(from_page["LoadingPage"].txt_statistics_number_of_checked_portions())
   # try:
   #    assert statistics_number_of_checked_portions_before + 1 == statistics_number_of_checked_portions_after
   # except AssertionError:
   #    print("Soft assert failed: Expected value not met.")

   # page.get_by_text("טעינות למעריך").click()
   # statistics_number_of_checked_portions_after = from_page["Functions"].extracting_value_from_statistics(initialize_pages["LoadingPage"].txt_statistics_number_of_checked_portions())
   # statistics_number_of_unchecked_portions_after = from_page["Functions"].extracting_value_from_statistics((initialize_pages["LoadingPage"].txt_statistics_number_of_unchecked_portions()))
   # statistics_number_of_checked_notebooks_after = from_page["Functions"].extracting_value_from_statistics((initialize_pages["LoadingPage"].txt_statistics_checked_notebooks()))
   # statistics_number_of_unchecked_notebooks_after = from_page["Functions"].extracting_value_from_statistics((initialize_pages["LoadingPage"].txt_statistics_unchecked_notebooks()))
   #
   # assert statistics_number_of_checked_portions_before +1 == statistics_number_of_checked_portions_after
   # assert statistics_number_of_unchecked_portions_before +1 == statistics_number_of_unchecked_portions_after
   # assert statistics_number_of_checked_notebooks_before +1 == statistics_number_of_checked_notebooks_after
   # assert statistics_number_of_unchecked_notebooks_before +1 == statistics_number_of_unchecked_notebooks_after


