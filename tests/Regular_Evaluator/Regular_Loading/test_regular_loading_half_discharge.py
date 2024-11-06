import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage


@pytest.mark.regular_loading
@pytest.mark.regular_evaluator
@allure.story("Half Discharge Process for Regular Loading - Regular Evaluator")
@allure.description("Half Discharge Process")
def test_regular_loading_half_discharge(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(regular_loading_number_E2E_half_discharge, 'regular_loading_number_E2E_half_discharge')

    f.functions.wait_for_networkidle()
    f.workflow.navigation_to_loading_screen()
    f.functions.search_loading(regular_loading_number_E2E_half_discharge)
    f.functions.table_choose_a_row(2).dblclick()
    # f.functions.table_choose_a_row(2).dblclick()
    # f.workflow.navigation_from_loading_to_CheckNotebookPage(2,2,2)

    #CheckNotebookScreen
    # f.workflow.notebook_checking_process()
    # f.functions.popup_answer_law()

    ###########################################################################################################################################
                                                                    # Testing
    #PortionScreen
    # f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()
    f.workflow.half_discharge_process()

    soft_assert.assert_all()
