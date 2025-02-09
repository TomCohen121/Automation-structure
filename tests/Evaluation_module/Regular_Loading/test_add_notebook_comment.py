import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.regular_loading
@allure.story("Add Comment to Notebook")
@allure.description("Adding a Comment to notebook using the 'Add comment' button")
def test_add_notebook_comment(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.choose_filter_option("טעינה להערכה")
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebook
    f.workflow.add_notebook_comment()
    notebook_comment = f.checkNotebookPage.txt_first_comment()
    assert notebook_comment == "tom"