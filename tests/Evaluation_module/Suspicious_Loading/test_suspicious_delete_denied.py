import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.suspicious_loading #C20750
@allure.story("Delete Notebook Suspicious Denied - Suspicious Loading")
@allure.description("Delete Notebook Suspicious Denied For Suspicious Notebook Using the 'Delete Notebook Check' button")
def test_suspicious_delete_approve(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(suspicious_loading_num,'suspicious_loading_num')
   # Dashboard
   f.workflow.navigation_to_loading_screen()

   # LoadingScreen
   f.functions.search_loading(suspicious_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

   # CheckNotebookScreen
   f.functions.click_delete_notebook_if_enable_suspicious()
   f.workflow.notebook_suspicion_denied_process()
   f.functions.popup_answer_law()
   f.functions.table_choose_a_row(2).dblclick()
   f.functions.click_delete_notebook_if_enable_suspicious()
   assert f.checkNotebookPage.txt_approve_and_denied_tag().count() == 0
   f.breadcrumbs.btn_breadcrumbs_to_notebooks_page().click()

   # NotebookScreen
   f.functions.assert_is_checkbox_checked(f.suspiciousLoadingNotebookPage.checkbox_notebook_suspicious_denied(2), expected_checked=False)
   f.functions.assert_equal_to(f.suspiciousLoadingNotebookPage.txt_suspicious_notebook_status(2),"מחברת נשלחה לבדיקה", "the Notebook status is not 'מחברת נשלחה לבדיקה'")

   soft_assert.assert_all()