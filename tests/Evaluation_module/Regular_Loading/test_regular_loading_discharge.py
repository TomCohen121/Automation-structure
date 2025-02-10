import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.regular_loading_discharge
@allure.story("Regular loading discharge")
@allure.description("Regular Notebook Checking and Regular Loading Discharge Process")
def test_regular_loading_discharge(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(regular_loading_for_discharge, 'regular_loading_for_discharge')
   #Dashboard
   num_of_discharged_loadings_before = f.functions.convert_to_int_from_str_or_number(f.personalAreaPage.txt_num_of_discharged_loadings())
   num_of_discharged_portions_before = f.functions.convert_to_int_from_str_or_number(f.personalAreaPage.txt_num_of_discharged_portions())
   num_of_discharged_notebooks_before = f.functions.convert_to_int_from_str_or_number(f.personalAreaPage.txt_num_of_discharged_notebooks())
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(regular_loading_for_discharge)
   f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

   #CheckNotebookScreen
   f.functions.click_delete_notebook_if_enable()
   f.workflow.notebook_checking_process()

   ##################################################################################################################################################################################
                                                                           # Testing
   #NotebookScreen
   f.functions.popup_answer_law()
   f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

   #ArchiveScreen
   f.workflow.loading_discharge_and_navigate_to_archive()
   f.functions.search_loading(regular_loading_for_discharge)
   f.functions.reload_page()
   f.functions.assert_element_exists(f.functions.table_choose_a_row(2),"the loading exist")
   f.breadcrumbs.btn_breadcrumbs_to_personal_area_page().click()

   #Dashboard
   num_of_discharged_loadings_after = f.functions.convert_to_int_from_str_or_number(f.personalAreaPage.txt_num_of_discharged_loadings())
   num_of_discharged_portions_after = f.functions.convert_to_int_from_str_or_number(f.personalAreaPage.txt_num_of_discharged_portions())
   num_of_discharged_notebooks_after = f.functions.convert_to_int_from_str_or_number(f.personalAreaPage.txt_num_of_discharged_notebooks())
   f.functions.assert_equal_to(num_of_discharged_loadings_before+1 ,num_of_discharged_loadings_after , "Dashboard statistics: Number of discharged loadings is Incorrect")
   f.functions.assert_equal_to(num_of_discharged_portions_before+1 ,num_of_discharged_portions_after , "Dashboard statistics: Number of discharged portions is Incorrect")
   f.functions.assert_equal_to(num_of_discharged_notebooks_before+1 ,num_of_discharged_notebooks_after , "Dashboard statistics: Number of discharged notebooks is Incorrect")

   soft_assert.assert_all()

