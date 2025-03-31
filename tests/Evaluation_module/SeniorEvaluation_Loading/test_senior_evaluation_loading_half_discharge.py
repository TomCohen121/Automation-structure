import allure
from pytest_playwright.pytest_playwright import page

from helper.soft_assert import soft_assert
from helper.utils import *


# @pytest.mark.senior_loading #C22677
@allure.story("Half Discharge Process for Senior Loading")
@allure.description("Half Discharge Process For Senior Notebook")
def test_senior_loading_half_discharge(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(senior_loading_num, 'senior_loading_num')
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(senior_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

    #CheckNotebookScreen
    f.functions.questions_numbers_finish_popup()
    f.functions.click_delete_notebook_if_enabled()
    f.workflow.senior_notebook_checking_process()

    ###########################################################################################################################################
                                                                    # Testing
    # NotebookScreen
    f.functions.popup_answer_law()
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    # PortionScreen
    f.workflow.assert_and_perform_half_discharge()

    soft_assert.assert_all()
