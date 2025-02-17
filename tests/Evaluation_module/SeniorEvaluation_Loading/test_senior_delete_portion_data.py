import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.senior_loading
@allure.story("Delete Portion Data - Senior Loading")
@allure.description("Deleting the Portion Data using the 'Delete Portion data' button")
def test_senior_delete_portion_data(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(senior_loading_num, 'senior_loading_num')
    # Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(senior_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebookScreen
    f.functions.questions_numbers_finish_popup()
    f.functions.click_delete_notebook_if_enable()
    f.workflow.senior_notebook_checking_process()

    ##################################################################################################################################################################################
                                                                 # Testing
    # NotebookScreen
    f.functions.popup_answer_law()
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    # PortionScreen
    f.workflow.delete_portion_data()
    table_num_of_checked_notebooks_after = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))
    f.functions.assert_equal_to(table_num_of_checked_notebooks_after,0, "Number of checked Notebooks is incorrect")
    table_avg_grade_after = f.functions.number_to_int(f.portionPage.txt_table_avg_grade(2))
    f.functions.assert_equal_to(table_avg_grade_after,0, "The Portion Average grade incorrect")
    f.functions.assert_equal_to(f.portionPage.txt_table_portion_status(2), "מנה נשלחה לבדיקה","the Portion status is not 'מנה נשלחה לבדיקה'")

    soft_assert.assert_all()



