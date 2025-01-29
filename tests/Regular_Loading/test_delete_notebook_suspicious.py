import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.regular_loading
@allure.story("Delete Notebook Suspicious")
@allure.description("Deleting the notebook's Suspicious using the 'Delete Notebook Check' button")
def test_delete_notebook_suspicious(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.choose_filter_option("טעינה להערכה")
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebookScreen
    f.workflow.delete_notebook_test()
    f.workflow.flow_set_suspicious_notebook()
    f.workflow.answer_one_question()
    f.functions.wait_for_element(f.checkNotebookPage.btn_delete_notebook_test())
    f.workflow.delete_notebook_test()
    f.workflow.assert_check_notebook_suspicious_deleted()
