import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *


@pytest.mark.afterappeal_loading #C20975
@allure.story("Add Comment to Notebook - AfterAppeal Loading")
@allure.description("Adding a Comment to notebook using the 'Add comment' button")
def test_afterappeal_add_notebook_comment(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(appeal_loading_num, 'appeal_loading_num')
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(appeal_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebook
    f.workflow.assert_add_notebook_comment_and_check()