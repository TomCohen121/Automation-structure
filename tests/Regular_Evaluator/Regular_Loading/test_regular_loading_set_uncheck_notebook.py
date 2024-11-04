import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage
from tests.conftest import from_page


@pytest.mark.regular_evaluator2
@allure.story("בדיקת אי בדיקה למחברת הערכה רגילה - מעריך רגיל")
@allure.description("תהליך אי בדיקה למחברת")
def test_regular_loading_set_uncheck_notebook(from_page, add_allure_attach, page):
    from_page["Functions"].wait_for_domcontentloaded()
    from_page["WorkFlow"].navigation_to_loading_screen()
    from_page["Functions"].search_loading(regular_loading_number)

    #LoadingScreen
    from_page["Functions"].table_choose_a_row(2).click()
    stat_num_of_nocheck_portions_before = from_page["Functions"].extracting_value_from_statistics(from_page["LoadingPage"].txt_stat_num_of_nocheck_portions())
    stat_num_of_nocheck_notebooks_before = from_page["Functions"].extracting_value_from_statistics(from_page["LoadingPage"].txt_stat_nocheck_notebooks())
    from_page["Functions"].table_choose_a_row(2).dblclick()

    # PortionScreen
    from_page["Functions"].table_choose_a_row(2).dblclick()

    # NotebookScreen
    from_page["Functions"].popup_answer_law()
    from_page["Functions"].table_choose_a_row(2).dblclick()

    # CheckNotebookScreen
    from_page["WorkFlow"].flow_set_uncheck_notebook()
    from_page["Functions"].popup_answer_law()
    ######################################################################################################################################################
                                                                # Testing

    # NotebookScreen
    from_page["Functions"].table_choose_a_row(2).click()
    notebook_status = from_page["NotebookPage"].txt_table_notebook_status(2).strip()
    from_page["Functions"].assert_equal_to(notebook_status,from_page["WorkFlow"].uncheck_reason,"The Notebook Status is not equal to the uncheck reason")
    from_page["Breadcrumbs"].btn_breadcrumbs_to_loadings_page().click()

    #LoadingScreen
    stat_num_of_nocheck_portions_after = from_page["Functions"].extracting_value_from_statistics(from_page["LoadingPage"].txt_stat_num_of_nocheck_portions())
    stat_num_of_nocheck_notebooks_after = from_page["Functions"].extracting_value_from_statistics(from_page["LoadingPage"].txt_stat_nocheck_notebooks())
    from_page["Functions"].assert_equal_to(stat_num_of_nocheck_notebooks_before+1,stat_num_of_nocheck_notebooks_after, "Statistics: Number of uncheck portions is incorrect")
    from_page["Functions"].assert_equal_to(stat_num_of_nocheck_portions_before+1,stat_num_of_nocheck_portions_after, "Statistics: Number of uncheck notebooks is incorrect")

    # from_page["WorkFlow"].loading_discharge_and_navigate_to_archive()
    #ArchiveScreen
    # from_page["Functions"].search_loading(regular_loading_number)
    # soft_assert.check(from_page["Functions"].table_choose_a_row(2).is_visible(),"The loading didn't appear in the archives")

    soft_assert.assert_all()

