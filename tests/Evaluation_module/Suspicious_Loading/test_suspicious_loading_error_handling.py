import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.soft_assert import soft_assert
from helper.utils import *


@pytest.mark.suspicious_loading #C22672
@allure.story("Error Handling Test for Suspicious Loading")
@allure.description("Error Handling Checking Process For Suspicious Notebook")
def test_suspicious_loading_error_handling(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(suspicious_loading_num,'suspicious_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(suspicious_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

   ###########################################################################################################################################
                                                                    # Testing
   #CheckNotebookScreen
   f.functions.click_delete_notebook_if_enabled_suspicious()
   f.workflow.assert_and_validate_popup_and_error_messages_suspicious_loading()
   soft_assert.assert_all()