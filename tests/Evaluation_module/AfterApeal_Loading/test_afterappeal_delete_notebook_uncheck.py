import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.soft_assert import soft_assert
from helper.utils import *


@pytest.mark.afterappeal_loading #C20996
@allure.story("Delete Notebook UnCheck - AfterAppeal Loading")
@allure.description("Deleting the notebook's UnCheck using the 'Delete Notebook Check' button")
def test_afterappeal_delete_notebook_uncheck(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(appeal_loading_num, 'appeal_loading_num')
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(appeal_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebookScreen
    f.functions.click_delete_notebook_if_enabled()
    f.workflow.flow_set_uncheck_notebook()
    f.workflow.delete_notebook_test()
    f.workflow.assert_check_notebook_uncheck_deleted()
    f.checkNotebookPage.btn_x_uncheck_notebook_popup().click()
    f.breadcrumbs.btn_breadcrumbs_to_notebooks_page().click()

    #NotebookScreen
    f.functions.popup_answer_law()
    table_num_of_checked_questions_after = f.functions.number_to_int(f.notebookPage.txt_table_num_of_checked_questions(2))
    table_notebook_grade_after = f.functions.number_to_int(f.notebookPage.txt_table_notebook_grade(2))
    f.functions.assert_equal_to(table_num_of_checked_questions_after,0, "Number of checked Questions is incorrect")
    f.functions.assert_equal_to(f.notebookPage.txt_table_notebook_status(2), "מחברת נשלחה לבדיקה","the Notebook status is not 'מחברת נשלחה לבדיקה'")
    f.functions.assert_equal_to(table_notebook_grade_after,0, "The Notebook grade is incorrect")
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    #PortionScreen
    table_num_of_checked_notebooks_after = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))
    f.functions.assert_equal_to(table_num_of_checked_notebooks_after,0, "Number of checked Notebooks is incorrect")
    f.functions.assert_equal_to(f.portionPage.txt_table_portion_status(2), "מנה נשלחה לבדיקה","the Portion status is not 'מנה נשלחה לבדיקה'")

    soft_assert.assert_all()

