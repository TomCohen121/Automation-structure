import re

import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.regular_loading
@allure.story("Add Comment to Notebook")
@allure.description("Adding a Comment to notebook using the 'Add comment' buttn")
def test_delete_notebook_uncheck(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.choose_filter_option("טעינה להערכה")
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebook
    f.checkNotebookPage.btn_add_comment().click()
    f.checkNotebookPage.field_comment_text().fill("tom")
    f.checkNotebookPage.btn_save_comment().click()
    f.checkNotebookPage.btn_all_comments().click()
    comment = f.checkNotebookPage.txt_first_comment()
    assert comment == "tom"