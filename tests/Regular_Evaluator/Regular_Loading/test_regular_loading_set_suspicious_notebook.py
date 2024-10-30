import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage
from tests.conftest import from_page


@pytest.mark.regular_evaluator2
@allure.story("בדיקת החשדת מחברת הערכה רגילה - מעריך רגיל")
@allure.description("תהליך החשדת מחברת")
def test_regular_loading_set_suspicious_notebook(from_page, add_allure_attach, page):
    from_page["Functions"].wait_for_domcontentloaded()
    from_page["WorkFlow"].navigation_to_loading_screen()
    from_page["Functions"].search_loading(regular_loading_number)

    #LoadingScreen
    from_page["Functions"].table_choose_a_row(2).click()
    statistics_number_of_suspicious_notebook_before = from_page["Functions"].extracting_value_from_statistics(from_page["LoadingPage"].txt_statistics_suspicious_notebooks())
    from_page["Functions"].table_choose_a_row(2).dblclick()

    #PortionScreen
    from_page["Functions"].table_choose_a_row(2).click()
    table_number_of_notebooks_in_suspicious_before = from_page["Functions"].number_to_int(from_page["PortionPage"].txt_table_number_of_suspicious_notebooks(2))
    from_page["Functions"].table_choose_a_row(2).dblclick()

    #NotebookScreen
    from_page["Functions"].popup_answer_law()
    from_page["Functions"].table_choose_a_row(2).dblclick()

    #CheckNotebookScreen
    from_page["WorkFlow"].flow_set_suspicious_notebook()
    from_page["WorkFlow"].notebook_checking_process()
    from_page["Functions"].popup_answer_law()
    #################################################################################################################################################
                                                                #Testing
    #NotebookScreen
    from_page["Functions"].checkbox_is_checked(from_page["NotebookPage"].checkbox_notebook_suspicious_evaluation(2),expected_state=True)
    from_page["Breadcrumbs"].btn_breadcrumbs_to_portions_page().click()

    #PortionScreen
    table_number_of_notebooks_in_suspicious_after = from_page["Functions"].number_to_int(from_page["PortionPage"].txt_table_number_of_suspicious_notebooks(2))
    from_page["Functions"].assert_equal_to(table_number_of_notebooks_in_suspicious_before+1,table_number_of_notebooks_in_suspicious_after , "Number of notebooks in Suspicious is incorrect")
    from_page["Breadcrumbs"].btn_breadcrumbs_to_loadings_page().click()

    #LoadingScreen
    statistics_number_of_suspicious_notebooks_after = from_page["Functions"].extracting_value_from_statistics(from_page["LoadingPage"].txt_statistics_suspicious_notebooks())
    from_page["Functions"].assert_equal_to(statistics_number_of_suspicious_notebook_before+1,statistics_number_of_suspicious_notebooks_after, "Number of Suspicious notebooks is incorrect")

    # from_page["WorkFlow"].loading_discharge_and_navigate_to_archive()
    # #ArchiveScreen
    # from_page["Functions"].search_loading(regular_loading_number)
    # soft_assert.check(from_page["Functions"].table_choose_a_row(2).is_visible(),"The loading didn't appear in the archives")

    soft_assert.assert_all()




