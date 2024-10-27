import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert


@pytest.mark.regular_evaluator
@allure.story("בדיקת E2E הערכה רגילה - מעריך רגיל")
@allure.description("תהליך בדיקת מחברת ופריקה של הטעינה")
def test_regular_loading_error_handling(from_page, add_allure_attach, page):
   from_page["Functions"].wait_for_domcontentloaded()
   from_page["WorkFlow"].navigation_to_loading_screen()
   # from_page["WorkFlow"].filters_new_loading_search()
   from_page["Functions"].search_loading(regular_loading_number)
   from_page["Functions"].table_choose_a_row(2).dblclick()
   from_page["Functions"].table_choose_a_row(3).dblclick()
   from_page["Functions"].table_choose_a_row(2).dblclick()

   from_page["CheckNotebookPage"].btn_save_and_end_notebook_test().click()
   from_page["Functions"].assert_verify_popup_error_message(from_page["CheckNotebookPage"].popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
   from_page["CheckNotebookPage"].btn_txt_saving_notebook_error_message_close().click()
   from_page["Functions"].notebook_pagination_loop()
   from_page["CheckNotebookPage"].btn_save_and_end_notebook_test().click()
   from_page["Functions"].assert_verify_popup_error_message(from_page["CheckNotebookPage"].popup_saving_notebook_error_message(),"יש להזין ציון לפחות לשאלה אחת")

   soft_assert.assert_all()
