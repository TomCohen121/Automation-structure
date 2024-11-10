import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.afterappeal_loading
@pytest.mark.regular_evaluator
@allure.story("Error Handling Test for AfterAppeal Loading - Regular Evaluator")
@allure.description("Error Handling Checking Process")
def test_afterappeal_loading_error_handling(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(after_appeal_number_error_handling,'after_appeal_number_error_handling')
   f.functions.wait_for_networkidle()
   f.workflow.navigation_to_loading_screen()
   f.functions.search_loading(after_appeal_number_error_handling)

   f.workflow.navigation_from_loading_to_CheckNotebookPage(2,2,2)

   ###########################################################################################################################################
                                                                    # Testing

   f.workflow.assert_and_validate_popup_and_error_messages_regular_loading()
   soft_assert.assert_all()
