import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.regular_loading
@allure.story("Error Handling Test for Regular loading")
@allure.description("Error Handling Checking Process")
def test_regular_loading_error_handling(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(regular_loading_E2E_num,'regular_loading_E2E_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(regular_loading_E2E_num)
   f.workflow.navigation_from_loading_to_CheckNotebookPage(2,2,2)

   ###########################################################################################################################################
                                                                    # Testing

   f.workflow.assert_and_validate_popup_and_error_messages_regular_loading()
   soft_assert.assert_all()
