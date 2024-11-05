import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage


@pytest.mark.regular_evaluator2
@allure.story("פריקה חלקית הערכה רגילה - מעריך רגיל")
@allure.description("תהליך פריקה חלקית")
def test_regular_loading_half_discharge(f, add_allure_attach, page):
    f.functions.wait_for_networkidle()
    f.workflow.navigation_to_loading_screen()
    f.functions.search_loading(regular_loading_number_E2E_half_discharge)
    f.functions.table_choose_a_row(2).dblclick()

    f.workflow.navigation_from_loading_to_checknotebookpage(2,2,2)

    #CheckNotebookScreen
    f.workflow.notebook_checking_process()
    f.functions.popup_answer_law()

    ###########################################################################################################################################
                                                                    # Testing
    #PortionScreen
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()
    f.functions.check_if_button_enabled_and_click(f.portionPage.btn_half_discharge_loading(),"The half discharged button is not clickable")

    #LoadingScreen
    f.portionPage.btn_save_loading_half_discharge_popup().click()
    f.functions.check_row_disabled_soft_assert(f.functions.table_choose_a_row(2),"The Portion is still Enable - The half discharge dosent Action dosent work")

    soft_assert.assert_all()
