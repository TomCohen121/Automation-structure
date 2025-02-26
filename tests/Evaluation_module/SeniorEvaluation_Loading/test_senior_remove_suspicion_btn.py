import sys
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.senior_loading #C25246
@allure.story("Remove Suspicion for Senior Loading")
@allure.description("Remove Suspicion for Senior Loading - Using the 'Remove Suspicion' Button")
def test_senior_remove_suspicion_btn(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(senior_loading_num, 'senior_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()
   #LoadingScreen
   f.functions.search_loading(senior_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

   #CheckNotebookScreen
   f.functions.click_delete_notebook_if_enable()
   f.workflow.assert_remove_suspicion_button()


