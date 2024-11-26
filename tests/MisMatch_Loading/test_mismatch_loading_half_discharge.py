import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage


@pytest.mark.mismatch_loading
@allure.story("Half Discharge Process for MisMatch Loading")
@allure.description("Mismatch Notebook Half Discharge Process")
def test_mismatch_loading_half_discharge(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(misMatch_loading_half_discharge_num, 'misMatch_loading_half_discharge_num')
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(misMatch_loading_half_discharge_num)
    f.workflow.navigation_from_loading_to_CheckNotebookPage(2,2,2)

    #CheckNotebookScreen
    f.workflow.mismatch_notebook_checking_process()

    ###########################################################################################################################################
                                                                    # Testing
    # NotebookScreen
    f.functions.popup_answer_law()
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    # PortionScreen
    f.workflow.assert_and_perform_half_discharge()
    soft_assert.assert_all()
