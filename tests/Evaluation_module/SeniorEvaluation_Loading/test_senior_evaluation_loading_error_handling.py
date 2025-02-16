import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.senior_loading
@allure.story("Error Handling Test for Senior loading - Senior Evaluator")
@allure.description("Senior Notebook Error Handling Checking Process")
def test_senior_loading_error_handling(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(senior_loading_num,'senior_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(senior_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

   ###########################################################################################################################################
                                                                # Testing
   #CheckNotebookScreen
   f.functions.questions_numbers_finish_popup()
   f.functions.click_delete_notebook_if_enable()
   f.workflow.assert_and_validate_popup_and_error_messages_senior_loading()
   soft_assert.assert_all()
