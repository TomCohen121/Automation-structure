import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from helper.configuration_manager import ConfigurationManager  # Import the ConfigurationManager
from pages.base_page import BasePage


@pytest.mark.regular_evaluator
@allure.story("בדיקת שגיאות הערכה רגילה - מעריך רגיל")
@allure.description("תהליך בדיקת שגיאות של הטעינה")
def test_regular_loading_error_handling(from_page, add_allure_attach, page):
   ConfigurationManager.load_config()


   from_page["Functions"].wait_for_domcontentloaded()
   from_page["WorkFlow"].navigation_to_loading_screen()
   # from_page["WorkFlow"].filters_new_loading_search()
   from_page["Functions"].search_loading(regular_loading_number)
   from_page["WorkFlow"].flow_from_loading_to_checknotebookpage(2,2,2)

   # ##########################################################################################################################################
                                                                    # Testing

   from_page["WorkFlow"].assert_and_validate_popup_and_error_messages()
   soft_assert.assert_all()
