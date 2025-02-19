import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.soft_assert import soft_assert
from helper.utils import *


@pytest.mark.permissions_system_administrator
@allure.story("Permissions for System Administrator")
@allure.description("Checking Permissions for System Administrator")
def test_permissions_for_system_administrator(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    # LoadingScreen
    f.functions.choose_filter_option("טעינה להערכה")
    f.functions.search_loading(regular_loading_num)
    f.functions.assert_element_exists(f.permissions.btn_loading_archive(), "The Button - מעבר לארכיון טעינות")
    f.functions.assert_element_exists(f.permissions.btn_loading_discharge(), "The Button - סיום בדיקה ושליחה למרבד")
    f.functions.assert_element_exists(f.permissions.btn_reset_loading_to_starting_state(),"The Button - החזר טעינה למצב התחלתי")
    f.functions.table_choose_a_row(2).dblclick()

    # PortionScreen
    f.functions.assert_element_exists(f.permissions.btn_half_discharge_loading(), "The Button - פריקה חלקית")
    f.functions.assert_element_exists(f.permissions.btn_delete_all_evaluations(),"The Button - מחק כלל הערכות במנה in Portion screen")
    f.functions.assert_element_exists(f.permissions.btn_confirm_no_check(), "The Button - אשר אי בדיקה")
    f.functions.assert_element_exists(f.permissions.btn_cancel_no_check(), "The Button - בטל אי בדיקה")
    f.functions.table_choose_a_row(2).dblclick()

    # NotebookScreen
    f.functions.popup_answer_law()
    f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation(),"The Button - מחק בדיקת מחברת in Notebook Page")
    f.functions.assert_element_exists(f.permissions.btn_end_notebook_evaluation(), "The Button - סיים בדיקת מנה")
    f.functions.table_choose_a_row(2).dblclick()

    # CheckNotebookScreen
    f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation_check_notebook(), "The Button - מחק בדיקת מחברת in CheckNotebook Page")
    f.functions.assert_element_exists(f.permissions.btn_student_adaptations(), "The Button - התאמות לתלמיד")
    f.functions.assert_element_exists(f.permissions.btn_show_formats(), "The Button - הצג פורמטים")
    f.functions.assert_element_exists(f.permissions.btn_uncheck_notebook(), "The Button - אי בדיקת מחברת")
    f.functions.assert_element_exists(f.permissions.btn_suspicious_notebook(), "The Button - מחברת חשודה")
    f.functions.assert_element_exists(f.permissions.btn_save_and_end_notebook_test(),"The Button - שמור וסיים בדיקת מחברת")
    f.functions.assert_element_exists(f.permissions.btn_save_question_score(), "The Button - שמור - in Grade Component")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

    #################################################################################################################################################

    #LoadingScreen
    f.functions.choose_filter_option("טעינה להערכה בכירה")
    f.functions.search_loading(senior_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    #PortionScreen
    f.functions.assert_element_exists(f.permissions.btn_half_discharge_loading(), "The Button - פריקה חלקית")
    f.functions.assert_element_exists(f.permissions.btn_delete_all_evaluations(), "The Button - מחק כלל הערכות במנה in Portion screen")
    f.functions.assert_element_exists(f.permissions.btn_confirm_no_check(), "The Button - אשר אי בדיקה")
    f.functions.assert_element_exists(f.permissions.btn_cancel_no_check(), "The Button - בטל אי בדיקה")
    f.functions.table_choose_a_row(2).dblclick()

    #NotebookScreen
    f.functions.popup_answer_law()
    f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation(), "The Button - מחק בדיקת מחברת in Notebook Page")
    f.functions.assert_element_exists(f.permissions.btn_end_notebook_evaluation(), "The Button - סיים בדיקת מנה")
    f.functions.table_choose_a_row(2).dblclick()

    #CheckNotebookScreen
    f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation_check_notebook(), "The Button - מחק בדיקת מחברת in CheckNotebook Page")
    f.functions.assert_element_exists(f.permissions.btn_student_adaptations(), "The Button - התאמות לתלמיד")
    f.functions.assert_element_exists(f.permissions.btn_show_formats(), "The Button - הצג פורמטים")
    f.functions.assert_element_not_exists(f.permissions.btn_uncheck_notebook(),"The Button - אי בדיקת מחברת")
    f.functions.assert_element_exists(f.permissions.btn_suspicious_notebook(), "The Button - מחברת חשודה")
    f.functions.assert_element_exists(f.permissions.btn_save_and_end_notebook_test(), "The Button - שמור וסיים בדיקת מחברת")
    f.functions.assert_element_exists(f.permissions.btn_save_question_score(), "The Button - שמור - in Grade Component")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()
    #################################################################################################################################################

    # LoadingScreen
    f.functions.choose_filter_option("טעינה לאי התאמה")
    f.functions.search_loading(misMatch_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    # PortionScreen
    f.functions.assert_element_exists(f.permissions.btn_half_discharge_loading(), "The Button - פריקה חלקית in Mismatch Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_delete_all_evaluations(),"The Button - מחק כלל הערכות במנה in Portion screen in Mismatch Loading")
    f.functions.assert_element_exists(f.permissions.btn_confirm_no_check(), "The Button - אשר אי בדיקה in Mismatch Loading")
    f.functions.assert_element_exists(f.permissions.btn_cancel_no_check(), "The Button - בטל אי בדיקה in Mismatch Loading")
    f.functions.table_choose_a_row(2).dblclick()

    # NotebookScreen
    f.functions.popup_answer_law()
    f.functions.assert_element_not_exists(f.permissions.btn_delete_notebook_evaluation(),"The Button - מחק בדיקת מחברת in Notebook Page in Mismatch Loading")
    f.functions.assert_element_exists(f.permissions.btn_end_notebook_evaluation(), "The Button - סיים בדיקת מנה in Mismatch Loading")
    f.functions.table_choose_a_row(2).dblclick()

    # CheckNotebookScreen
    f.functions.assert_element_not_exists(f.permissions.btn_delete_notebook_evaluation_check_notebook(),"The Button - מחק בדיקת מחברת in CheckNotebook Page in Mismatch Loading")
    f.functions.assert_element_exists(f.permissions.btn_student_adaptations(), "The Button - התאמות לתלמיד in Mismatch Loading")
    f.functions.assert_element_exists(f.permissions.btn_show_formats(), "The Button - הצג פורמטים in Mismatch Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_uncheck_notebook(), "The Button - אי בדיקת מחברת in Mismatch Loading")
    f.functions.assert_element_exists(f.permissions.btn_suspicious_notebook(), "The Button - מחברת חשודה in Mismatch Loading")
    f.functions.assert_element_exists(f.permissions.btn_save_and_end_notebook_test(),"The Button - שמור וסיים בדיקת מחברת in Mismatch Loading")
    f.functions.assert_element_exists(f.permissions.btn_save_question_score(), "The Button - שמור - in Grade Component in Mismatch Loading")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

    #################################################################################################################################################

    # LoadingScreen
    f.functions.choose_filter_option("טעינה לחשודים")
    f.functions.search_loading(suspicious_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    # PortionScreen
    f.functions.assert_element_exists(f.permissions.btn_half_discharge_loading(), "The Button - פריקה חלקית in Suspicious Loading")
    f.functions.assert_element_exists(f.permissions.btn_delete_all_evaluations(),"The Button - מחק כלל הערכות במנה in Portion screen in Suspicious Loading")
    f.functions.assert_element_exists(f.permissions.btn_confirm_no_check(), "The Button - אשר אי בדיקה in Suspicious Loading")
    f.functions.assert_element_exists(f.permissions.btn_cancel_no_check(), "The Button - בטל אי בדיקה in Suspicious Loading")
    f.functions.table_choose_a_row(2).dblclick()

    # NotebookScreen
    f.functions.popup_answer_law()
    f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation(), "The Button - מחק בדיקת מחברת in Notebook Page in Suspicious Loading")
    f.functions.assert_element_exists(f.permissions.btn_end_notebook_evaluation(), "The Button - סיים בדיקת מנה in Suspicious Loading")
    f.functions.table_choose_a_row(2).dblclick()

    # CheckNotebookScreen
    f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation_check_notebook(),"The Button - מחק בדיקת מחברת in CheckNotebook Page in Suspicious Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_suspicious_history(), "The Button - היסטוריית חשד in Suspicious Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_student_adaptations(), "The Button - התאמות לתלמיד in Suspicious Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_show_formats(), "The Button - הצג פורמטים in Suspicious Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_uncheck_notebook(), "The Button - אי בדיקת מחברת in Suspicious Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_suspicious_notebook(), "The Button - מחברת חשודה in Suspicious Loading")
    f.functions.assert_element_exists(f.permissions.btn_save_and_end_notebook_test(), "The Button - שמור וסיים בדיקת מחברת in Suspicious Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_save_question_score(), "The Button - שמור - in Grade Component in Suspicious Loading")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

    #################################################################################################################################################

    # LoadingScreen
    f.functions.choose_filter_option("טעינה לאחר ערעור")
    f.functions.search_loading(appeal_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    # PortionScreen
    f.functions.assert_element_exists(f.permissions.btn_half_discharge_loading(), "The Button - פריקה חלקית in AfterAppeal Loading")
    f.functions.assert_element_exists(f.permissions.btn_delete_all_evaluations(),"The Button - מחק כלל הערכות במנה in Portion screen in AfterAppeal Loading")
    f.functions.assert_element_exists(f.permissions.btn_confirm_no_check(), "The Button - אשר אי בדיקה in AfterAppeal Loading")
    f.functions.assert_element_exists(f.permissions.btn_cancel_no_check(), "The Button - בטל אי בדיקה in AfterAppeal Loading")
    f.functions.table_choose_a_row(2).dblclick()

    # NotebookScreen
    f.functions.popup_answer_law()
    f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation(),"The Button - מחק בדיקת מחברת in Notebook Page in AfterAppeal Loading")
    f.functions.assert_element_exists(f.permissions.btn_end_notebook_evaluation(), "The Button - סיים בדיקת מנה in AfterAppeal Loading")
    f.functions.table_choose_a_row(2).dblclick()

    # CheckNotebookScreen
    f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation_check_notebook(),"The Button - מחק בדיקת מחברת in CheckNotebook Page in AfterAppeal Loading")
    f.functions.assert_element_exists(f.permissions.btn_student_adaptations(), "The Button - התאמות לתלמיד in AfterAppeal Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_show_formats(), "The Button - הצג פורמטים in AfterAppeal Loading")
    f.functions.assert_element_exists(f.permissions.btn_uncheck_notebook(), "The Button - אי בדיקת מחברת in AfterAppeal Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_suspicious_notebook(), "The Button - מחברת חשודה in AfterAppeal Loading")
    f.functions.assert_element_exists(f.permissions.btn_save_and_end_notebook_test(), "The Button - שמור וסיים בדיקת מחברת in AfterAppeal Loading")
    f.functions.assert_element_exists(f.permissions.btn_save_question_score(), "The Button - שמור - in Grade Component in AfterAppeal Loading")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

    #################################################################################################################################################

    # LoadingScreen
    f.functions.choose_filter_option("טעינה למדגם לפני הערכה")
    f.functions.search_loading(assessment_loading_num)
    f.functions.table_choose_a_row(2).dblclick()

    # PortionScreen
    f.functions.assert_element_not_exists(f.permissions.btn_half_discharge_loading(), "The Button - פריקה חלקית in Assessment Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_delete_all_evaluations(),"The Button - מחק כלל הערכות במנה in Portion screen in Assessment Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_confirm_no_check(), "The Button - אשר אי בדיקה in Assessment Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_cancel_no_check(), "The Button - בטל אי בדיקה in Assessment Loading")
    f.functions.table_choose_a_row(2).dblclick()

    # NotebookScreen
    f.functions.popup_answer_law()
    f.functions.assert_element_not_exists(f.permissions.btn_delete_notebook_evaluation(),"The Button - מחק בדיקת מחברת in Notebook Page in Assessment Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_end_notebook_evaluation(), "The Button - סיים בדיקת מנה in Assessment Loading")
    f.functions.table_choose_a_row(2).dblclick()

    # CheckNotebookScreen
    f.functions.assert_element_not_exists(f.permissions.btn_delete_notebook_evaluation_check_notebook(),"The Button - מחק בדיקת מחברת in CheckNotebook Page in Assessment Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_student_adaptations(), "The Button - התאמות לתלמיד in Assessment Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_show_formats(), "The Button - הצג פורמטים in Assessment Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_uncheck_notebook(), "The Button - אי בדיקת מחברת in Assessment Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_suspicious_notebook(), "The Button - מחברת חשודה in Assessment Loading")
    f.functions.assert_element_not_exists(f.permissions.btn_save_and_end_notebook_test(),"The Button - שמור וסיים בדיקת מחברת in Assessment Loading")
    f.functions.assert_is_field_disabled(f.checkNotebookPage.field_question_number())

    soft_assert.assert_all()

