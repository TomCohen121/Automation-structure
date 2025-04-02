import allure
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

# @pytest.mark.regular_loading #C22673
@allure.story("Half Discharge Process for Regular Loading")
@allure.description("Regular Notebook Half Discharge Process")
def test_regular_loading_half_discharge(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(regular_loading_num, 'regular_loading_num')
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(regular_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

    #CheckNotebookScreen
    f.functions.click_delete_notebook_if_enabled()
    f.workflow.notebook_checking_process()

    ###########################################################################################################################################
                                                                    # Testing
    # NotebookScreen
    f.functions.popup_answer_law()
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    # PortionScreen
    f.workflow.assert_and_perform_half_discharge()

    soft_assert.assert_all()
