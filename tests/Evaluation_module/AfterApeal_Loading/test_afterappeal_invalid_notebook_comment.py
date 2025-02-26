import sys
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.afterappeal_loading #C20978
@allure.story("Invalid Notebook Comment for AfterAppeal Loading")
@allure.description("Invalid Notebook Comment for AfterAppeal Loading - Type Nothing in the Comment popup - Expecting to get an Error")
def test_afterappeal_invalid_comment(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(appeal_loading_num, 'appeal_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(appeal_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

   #CheckNotebookScreen
   f.workflow.assert_invalid_comment_error()