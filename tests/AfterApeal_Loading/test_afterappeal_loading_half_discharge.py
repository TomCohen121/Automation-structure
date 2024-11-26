import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage

@pytest.mark.afterappeal_loading
@allure.story("Half Discharge Process AfterAppeal Loading")
@allure.description("AfterAppeal Notebook Half Discharge Process")
def test_afterappeal_loading_half_discharge(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(appeal_loading_half_discharge_num, 'appeal_loading_half_discharge_num')
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(appeal_loading_half_discharge_num)
    f.workflow.navigation_from_loading_to_checknotebookpage(2,2,2)

    #CheckNotebookScreen
    f.workflow.notebook_checking_process()

    ###########################################################################################################################################
                                                                    # Testing
    # NotebookScreen
    f.functions.popup_answer_law()
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    # PortionScreen
    f.workflow.assert_and_perform_half_discharge()
    soft_assert.assert_all()
