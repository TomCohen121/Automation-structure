import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage
from tests.conftest import from_page


@pytest.mark.regular_evaluator2
@allure.story("פריקה חלקית הערכה רגילה - מעריך רגיל")
@allure.description("תהליך פריקה חלקית")
def test_regular_loading_half_discharge(from_page, add_allure_attach, page):
    from_page["Functions"].wait_for_domcontentloaded()
    from_page["WorkFlow"].navigation_to_loading_screen()
    from_page["Functions"].search_loading(regular_loading_number)
    from_page["Functions"].table_choose_a_row(2).dblclick()


    from_page["WorkFlow"].flow_from_loading_to_checknotebookpage(2,2,2)
    from_page["WorkFlow"].notebook_checking_process()
    from_page["Functions"].popup_answer_law()

    from_page["Breadcrumbs"].btn_breadcrumbs_to_portions_page().click()
    from_page["Functions"].check_if_button_enabled_and_click(from_page["PortionPage"].btn_half_discharge_loading(),"The half discharged button is not clickable")

    from_page["PortionPage"].btn_save_loading_half_discharge_popup().click()
    from_page["Functions"].check_row_disabled_soft_assert(from_page["Functions"].table_choose_a_row(2),"The Portion is still Enable - The half discharge dosent Action dosent work")

    soft_assert.assert_all()
