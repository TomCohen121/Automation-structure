import allure
import pytest
from allure_pytest.utils import allure_suite_labels
from pytest_playwright.pytest_playwright import page
from pages.base_page import BasePage


@pytest.mark.sanity
@allure.story("טסט 1")
@allure.description("תיאור טסט 1")
def test_normal_loading(initialize_pages, add_allure_attach, page):
   # initialize_pages['WorkFlow'].navigation_to_loading_screen()
   initialize_pages["PersonalAreaPage"].txt_search_box().fill("Tom")

# @allure.story("בדיקות עבור פיצ'ר C")
# def test_normal_loading_flow(playwright: Playwright):
    # functions.navigation_to_loading_screen()
    # functions.search_loading("0045518")
    #
    # loading_page.btn_table_choose_a_row(2).click()
    #
    # number_of_checked_portion_before = functions.number_of_checked_portions()
    # print(f'the number of checked qustion before is {number_of_checked_portion_before}')
    # unchecked_portions = loading_page.txt_statistics_number_of_unchecked_portions()
    # print(f'the number of unchecked portions is: {unchecked_portions}')
    # checked_notebooks = loading_page.txt_statistics_checked_notebooks()
    # print(f'the number of checked notebook is: {checked_notebooks}')
    # unchecked_notebooks = loading_page.txt_statistics_unchecked_notebooks()
    # print(f'the number of unchecked notebook is: {unchecked_notebooks}')
    #
    # loading_page.btn_table_choose_a_row(2).dblclick()
    # loading_page.btn_table_choose_a_row(2).dblclick()
    # functions.popup_answer_law()
    # loading_page.btn_table_choose_a_row(2).dblclick()
    # checked_notebooks = portion_page.txt_table_number_of_checked_notebooks(2)
    # print(f'the number of cheaked question is: {checked_notebooks}')
    # avg_grade = portion_page.txt_table_avg_grade(2)
    # print(f'the avg grade is {avg_grade}')
    # status = portion_page.txt_table_portion_status(2)
    # print(f'the status is {status}')

    # checked_questions = notebook_page.txt_table_number_of_checked_questions(3)
    # print(f'the number of the cheakde quistion is {checked_questions}')
    # notebook_grade = notebook_page.txt_table_notebook_grade(3)
    # print(f'the grade is {notebook_grade}')
    # notebook_status = notebook_page.txt_table_notebook_status(3)
    # print(f'the status is{notebook_status}')

    # check_notebook_page.field_question_number().fill("1")
    # functions.is_subquestion_exist()
    # check_notebook_page.field_question_score().fill("1")
    # check_notebook_page.btn_save_question().click()
    # functions.notebook_pagination_loop()
    # check_notebook_page.btn_save_and_end_notebook_test().click()
    # check_notebook_page.btn_save_notebook_popup().click()
    # check_notebook_page.btn_close_after_saving_notebook()
    # page.locator('[ng-reflect-router-link="/loadings-for-evaluator"]').click()
    #
    # number_of_checked_portion_after = functions.number_of_checked_portions()
    # print(f'the number of checked qustion after is {number_of_checked_portion_after}')
    # assert number_of_checked_portion_before +1 == number_of_checked_portion_after

