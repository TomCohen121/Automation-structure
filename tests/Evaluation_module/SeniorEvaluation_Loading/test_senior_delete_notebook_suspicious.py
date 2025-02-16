import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.senior_loading
@allure.story("Delete Notebook Suspicious - Senior Loading")
@allure.description("Deleting the notebook's Suspicious using the 'Delete Notebook Check' button")
def test_senior_delete_notebook_suspicious(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(senior_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebookScreen
    f.functions.questions_numbers_finish_popup()
    f.functions.click_delete_notebook_if_enable()
    f.workflow.flow_set_suspicious_notebook()
    f.functions.process_api_data(f.functions.fetch_api_data_senior)
    f.functions.wait_for_element(f.checkNotebookPage.btn_delete_notebook_test())
    f.workflow.delete_notebook_test()
    f.workflow.assert_check_notebook_suspicious_deleted()
