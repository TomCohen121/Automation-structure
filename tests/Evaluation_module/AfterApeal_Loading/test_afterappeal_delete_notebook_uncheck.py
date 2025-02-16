import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.afterappeal_loading
@allure.story("Delete Notebook UnCheck - AfterAppeal Loading")
@allure.description("Deleting the notebook's UnCheck using the 'Delete Notebook Check' button")
def test_afterappeal_delete_notebook_uncheck(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(appeal_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebookScreen
    f.functions.click_delete_notebook_if_enable()
    f.workflow.flow_set_uncheck_notebook()
    f.workflow.delete_notebook_test()
    f.workflow.assert_check_notebook_uncheck_deleted()


