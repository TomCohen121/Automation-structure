import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.tom
@pytest.mark.regular_loading
@pytest.mark.regular_evaluator
@allure.story("בדיקת שגיאות הערכה רגילה - מעריך רגיל")
@allure.description("תהליך בדיקת שגיאות של הטעינה")
def test_regular_loading_error_handling(f, add_allure_attach, page):
   f.functions.check_loading_number(regular_loading_number_error_handling,'regular_loading_number_error_handling')
   f.functions.wait_for_networkidle()
   f.workflow.navigation_to_loading_screen()
   f.functions.search_loading(regular_loading_number_error_handling)
   f.workflow.navigation_from_loading_to_CheckNotebookPage(2,2,2)

   ###########################################################################################################################################
                                                                    # Testing

   f.workflow.assert_and_validate_popup_and_error_messages()
   soft_assert.assert_all()
