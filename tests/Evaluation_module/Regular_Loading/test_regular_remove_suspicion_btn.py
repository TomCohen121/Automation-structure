import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *

@pytest.mark.regular_loading #C20703
@allure.story("Remove Suspicion for Regular Loading")
@allure.description("Remove Suspicion for Regular Loading - Using the 'Remove Suspicion' Button")
def test_regular_remove_suspicion_btn(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(regular_loading_num, 'regular_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()
   #LoadingScreen
   f.functions.search_loading(regular_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

   #CheckNotebookScreen
   f.functions.click_delete_notebook_if_enabled()
   f.workflow.assert_remove_suspicion_button()


