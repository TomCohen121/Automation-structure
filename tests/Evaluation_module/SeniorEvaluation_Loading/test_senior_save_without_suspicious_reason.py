import allure
import allure
import pytest
from pytest_playwright.pytest_playwright import page

from helper.utils import *


@pytest.mark.senior_loading #C20807
@allure.story("Save Suspicious Notebook without a Suspicious reason for Senior Loading")
@allure.description("Save Suspicious Notebook without a Suspicious reason for Senior Loading - Expecting to get an Error")
def test_senior_save_without_suspicious_reason(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(senior_loading_num, 'senior_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(senior_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

   #CheckNotebookScreen
   f.functions.click_delete_notebook_if_enabled()
   f.workflow.assert_invalid_suspicious_reason_error()


