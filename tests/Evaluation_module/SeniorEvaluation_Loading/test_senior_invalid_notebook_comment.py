import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *


@pytest.mark.senior_loading #C20771
@allure.story("Invalid Notebook Comment for Senior Loading")
@allure.description("Invalid Notebook Comment for Senior Loading - Type Nothing in the Comment popup - Expecting to get an Error")
def test_senior_invalid_comment(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(senior_loading_num, 'senior_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(senior_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

   #CheckNotebookScreen
   f.workflow.assert_invalid_comment_error()