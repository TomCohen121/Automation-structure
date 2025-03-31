import allure
import allure
import pytest
from pytest_playwright.pytest_playwright import page

from helper.utils import *


@pytest.mark.senior_loading #C20768
@allure.story("Add Comment to Notebook - Senior Loading")
@allure.description("Adding a Comment to notebook using the 'Add comment' button")
def test_senior_add_notebook_comment(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(senior_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebook
    f.functions.questions_numbers_finish_popup()
    f.workflow.assert_add_notebook_comment_and_check()