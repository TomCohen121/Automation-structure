import re
import time
from asyncio import wait_for
import allure
import pytest
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.suspicious_loading #C17638
@allure.story("Approve Uncheck Portion - Suspicious Loading")
@allure.description("Approve notebook UnCheck using the 'Approve uncheck' button")
def test_suspicious_approve_notebook_uncheck(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(suspicious_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    #PortionScreen
    f.functions.click_delete_portion_if_enable()
    f.portionPage.btn_approve_portion_uncheck().click()
    f.functions.table_choose_a_row(2).dblclick()
    assert f.portionPage.txt_table_portion_status(2) == "מנה סומנה כלא נבדקה"