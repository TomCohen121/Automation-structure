import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.mismatch_loading
@pytest.mark.regular_evaluator
@allure.story("E2E Test for MisMatch Loading - Regular Evaluator")
@allure.description("Notebook Checking and Loading Discharge Process")
def test_mismatch_loading_end_to_end(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(MisMatch_loading_E2E_num,'MisMatch_loading_E2E_num')

   #Dashboard
   # num_of_discharged_loadings_before = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_loadings())
   # num_of_discharged_portions_before = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_portions())
   # num_of_discharged_notebooks_before = f.functions.convert_to_int_from_str_or_number(f.personal_areaPage.txt_num_of_discharged_notebooks())

   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(MisMatch_loading_E2E_num)
   f.functions.table_choose_a_row(2).click()
   stat_num_of_checked_portions_before = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_checked_portions())
   stat_num_of_unchecked_portions_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_num_of_unchecked_portions()))
   stat_num_of_checked_notebooks_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_checked_notebooks()))
   stat_num_of_unchecked_notebooks_before = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_unchecked_notebooks()))
   f.functions.table_choose_a_row(2).dblclick()

   #PortionScreen
   table_num_of_checked_notebooks_before = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))
   f.functions.table_choose_a_row(2).dblclick()

   #NotebookScreen
   f.functions.popup_answer_law()
   f.functions.table_choose_a_row(2).dblclick()

   #CheckNotebookScreen
   f.workflow.answer_all_questions()