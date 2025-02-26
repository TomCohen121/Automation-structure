import sys
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.suspicious_loading #C20755
@allure.story("Save Uncheck without a reason for Suspicious Loading")
@allure.description("Save Uncheck without a reason for Suspicious Loading - Expecting to get an Error")
def test_suspicious_save_without_uncheck_reason(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(suspicious_loading_num, 'suspicious_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(suspicious_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

   #CheckNotebookScreen
   f.functions.click_delete_notebook_if_enable_suspicious()
   f.workflow.assert_invalid_uncheck_reason_error()


