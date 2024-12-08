import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.suspicious_loading
@allure.story("E2E Test for Suspicious Loading - Approve Notebook Suspicion")
@allure.description("Approve Notebook Suspicion and Loading Discharge Process For Suspicious Notebook")
def test_suspicious_loading_end_to_end_approve(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(suspicious_loading_approve_num,'suspicious_loading_approve_num')
   #Dashboard
   # num_of_discharged_loadings_before = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_loadings())
   # num_of_discharged_portions_before = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_portions())
   # num_of_discharged_notebooks_before = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_notebooks())
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(suspicious_loading_approve_num)
   f.functions.table_choose_a_row(2).click()
   stat_num_of_checked_portions_before = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_checked_portions())
   stat_num_of_unchecked_portions_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_num_of_unchecked_portions()))
   stat_num_of_checked_notebooks_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_checked_notebooks()))
   stat_num_of_unchecked_notebooks_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_unchecked_notebooks()))
   stat_num_of_suspicious_notebooks_before = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_suspicious_notebooks())
   f.functions.table_choose_a_row(2).dblclick()

   #PortionScreen
   table_num_of_suspicion_approved_before = f.functions.number_to_int(f.suspiciousLoadingPortionPage.txt_table_num_of_suspicion_approved(2))
   f.functions.table_choose_a_row(2).dblclick()

   #NotebookScreen
   f.functions.popup_answer_law()
   f.functions.table_choose_a_row(2).dblclick()

   # CheckNotebookScreen
   f.workflow.notebook_suspicion_approved_process()

   ##################################################################################################################################################################################
                                                                           # Testing
   #NotebookScreen
   f.functions.popup_answer_law()
   f.functions.is_checkbox_checked(f.suspiciousLoadingNotebookPage.checkbox_notebook_suspicious_approved(2),expected_state=True,error_message="The Suspicious Approved Check box should be Marked")
   f.functions.is_checkbox_checked(f.suspiciousLoadingNotebookPage.checkbox_notebook_suspicious_denied(2), expected_state=False , error_message="The Suspicious Denied Check box should be Unmarked")
   f.functions.assert_equal_to(f.suspiciousLoadingNotebookPage.txt_suspicious_notebook_status(2),"מחברת נבדקה", "the Notebook status is not 'מחברת נבדקה'")
   f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

   #PortionScreen
   f.functions.assert_equal_to(f.suspiciousLoadingPortionPage.txt_table_sus_portion_status(2),"מנה תקינה ממתינה למשיכת תפוקה","the Portion status is not 'מנה תקינה ממתינה למשיכת תפוקה'")
   table_num_of_suspicion_approved_after = f.functions.number_to_int(f.suspiciousLoadingPortionPage.txt_table_num_of_suspicion_approved(2))
   f.functions.assert_equal_to(table_num_of_suspicion_approved_before+1,table_num_of_suspicion_approved_after , "Number of Suspicion Approved Notebooks is incorrect")
   f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

   #LoadingScreen
   stat_num_of_checked_portions_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_checked_portions())
   stat_num_of_unchecked_portions_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_num_of_unchecked_portions()))
   stat_num_of_checked_notebooks_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_checked_notebooks()))
   stat_num_of_unchecked_notebooks_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_unchecked_notebooks()))
   stat_num_of_suspicious_notebooks_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_suspicious_notebooks())
   f.functions.assert_equal_to(stat_num_of_checked_portions_before +1, stat_num_of_checked_portions_after, "Statistics: Number of checked portions is incorrect")
   f.functions.assert_equal_to(stat_num_of_unchecked_portions_before -1, stat_num_of_unchecked_portions_after, "Statistics: Number of unchecked portions is incorrect")
   f.functions.assert_equal_to(stat_num_of_checked_notebooks_before +1, stat_num_of_checked_notebooks_after , "Statistics: Number of checked notebooks is incorrect")
   f.functions.assert_equal_to(stat_num_of_unchecked_notebooks_before -1, stat_num_of_unchecked_notebooks_after , "Statistics: Number of unchecked notebooks is incorrect")
   f.functions.assert_equal_to(stat_num_of_suspicious_notebooks_before + 1, stat_num_of_suspicious_notebooks_after, "Statistics: Number of Suspicious notebooks is incorrect")

   #ArchiveScreen
   # f.workflow.loading_discharge_and_navigate_to_archive()
   # f.functions.search_loading(suspicious_loading_approve_num)
   # soft_assert.check(f.functions.table_choose_a_row(2).is_visible(),"The loading didn't appear in the archives")
   # f.breadcrumbs.btn_breadcrumbs_to_personal_area_page().click()

   #Dashboard
   # num_of_discharged_loadings_after = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_loadings())
   # num_of_discharged_portions_after = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_portions())
   # num_of_discharged_notebooks_after = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_notebooks())
   # f.functions.assert_equal_to(num_of_discharged_loadings_before+1 ,num_of_discharged_loadings_after , "Dashboard statistics: Number of discharged loadings is Incorrect")
   # f.functions.assert_equal_to(num_of_discharged_portions_before+1 ,num_of_discharged_portions_after , "Dashboard statistics: Number of discharged portions is Incorrect")
   # f.functions.assert_equal_to(num_of_discharged_notebooks_before+1 ,num_of_discharged_notebooks_after , "Dashboard statistics: Number of discharged notebooks is Incorrect")

   soft_assert.assert_all()



