import allure
import pytest
from pytest_playwright.pytest_playwright import page, playwright
from helper.utils import *
from helper.soft_assert import soft_assert


@allure.story("Answer Law Test")
@allure.description("Answer Law Checking Process")
def test_answer_law(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(answer_law,'answer_law')
   #Dashboard
   f.workflow.navigation_to_loading_screen()

   # LoadingScreen
   f.functions.search_loading(answer_law)
   f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

   ###########################################################################################################################################
                                                                    # Testing

   #CheckNotebookScreen
   f.workflow.assert_and_validate_popup_and_error_messages_answer_law()

   soft_assert.assert_all()


