import time
from extensions.functions import Functions
from pages.base_page import BasePage
from playwright.sync_api import Page
from pages.check_notebook_page import CheckNotebookPage
from pages.loading_page import LoadingPage
from pages.notebook_page import NotebookPage
from pages.personal_area_page import PersonalAreaPage
from pages.portion_page import PortionPage
from pages.suspicious_loading_notebook_page import SuspiciousLoadingNotebookPage
from pages.suspicious_loading_portions_page import SuspiciousLoadingPortionPage


class WorkFlow(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)
       self.personalAreaPage = PersonalAreaPage(self.page)
       self.loadingPage = LoadingPage(self.page)
       self.checkNotebookPage = CheckNotebookPage(self.page)
       self.notebookPage = NotebookPage(self.page)
       self.portionPage = PortionPage(self.page)
       self.functions = Functions(self.page)
       self.suspiciousLoadingPortionPage = SuspiciousLoadingPortionPage(self.page)
       self.suspiciousLoadingNotebookPage = SuspiciousLoadingNotebookPage(self.page)

    # --------------------------- Notebooks Checking Process ---------------------------

   def notebook_checking_process_with_grade(self):
       self.checkNotebookPage.field_question_number().fill('1')
       self.checkNotebookPage.field_question_number().press('Enter')
       self.functions.is_subquestion_exist()
       self.checkNotebookPage.field_question_score().fill('6')
       self.checkNotebookPage.btn_maximum_grade().click()
       self.checkNotebookPage.btn_save_question_score().click()
       self.checkNotebookPage.txt_total_notebook_grade().wait_for(state="visible", timeout=5000)
       self.notebook_grade = self.functions.extracting_total_notebook_grade(self.checkNotebookPage.txt_total_notebook_grade())
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def notebook_checking_process(self):
       self.checkNotebookPage.field_question_number().fill('1')
       self.checkNotebookPage.field_question_number().press('Enter')
       self.functions.is_subquestion_exist()
       self.checkNotebookPage.field_question_score().fill('6')
       self.checkNotebookPage.btn_maximum_grade().click()
       self.checkNotebookPage.btn_save_question_score().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def mismatch_notebook_checking_process(self):
       self.functions.process_api_data(self.functions.fetch_api_data_mismatch)
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def senior_notebook_checking_process(self):
       self.functions.process_api_data(self.functions.fetch_api_data_senior)
       self.checkNotebookPage.btn_save_gap_successfully_closed().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   # def delete_notebook_test(self):
   #     if self.checkNotebookPage.btn_delete_notebook_test().is_enabled():
   #         self.checkNotebookPage.btn_delete_notebook_test().click()
   #         self.checkNotebookPage.btn_save_delete_notebook_test().click()
   #         self.functions.wait_for_loader()

    # --------------------------- Navigation Flows ---------------------------

   def navigation_from_loading_to_CheckNotebookPage(self,row_number,row_number1,row_number2):
       self.functions.table_choose_a_row(row_number).dblclick()
       self.functions.table_choose_a_row(row_number1).dblclick()
       self.functions.popup_answer_law()
       self.functions.table_choose_a_row(row_number2).dblclick()

   def navigation_to_loading_screen(self):
       self.personalAreaPage.btn_questionnaire_evaluation().click()
       self.personalAreaPage.btn_reception_screens().click()
       self.personalAreaPage.btn_loading_for_the_evaluator().click()

   def loading_discharge_and_navigate_to_archive(self):
        self.loadingPage.btn_loading_discharge().click()
        self.loadingPage.btn_save_loading_discharge_popup().click()
        self.loadingPage.btn_loading_archive().click()

    # --------------------------- Asserts Error Message Flows ---------------------------

   def assert_and_validate_popup_and_error_messages_regular_loading(self):
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(
       self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.assert_verify_popup_error_message(
       self.checkNotebookPage.popup_saving_notebook_error_message(), "יש להזין ציון לפחות לשאלה אחת")

   def assert_and_validate_popup_and_error_messages_suspicious_loading(self):
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(), "יש לאשר / לבטל חשד לפני סיום בדיקה")

   def assert_and_validate_popup_and_error_messages_senior_loading(self):
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(), "יש לסגור את הפער לפני סיום בדיקה")

   def assert_and_validate_popup_and_error_messages_mismatch_loading(self):
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       notebook_data = self.functions.fetch_api_data_mismatch()
       unanswered_questions = self.functions.extract_unanswered_descriptions(notebook_data)
       print(f"the queistons is {unanswered_questions}")
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(), f"לא הוזן ציון לכל השאלות, יש להזין ציון לשאלות: {unanswered_questions}")

    # --------------------------- Suspicious Notebook Flows ---------------------------

   def flow_set_suspicious_notebook(self):
       self.checkNotebookPage.btn_suspicious_notebook().click()
       self.checkNotebookPage.checkbox_mark_suspicious_notebook().check()
       self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_suspicious_reason(),self.checkNotebookPage.dropdown_suspicious_reason_list(),'div')
       self.checkNotebookPage.btn_choose_suspicious_dropdown_options().click()
       self.checkNotebookPage.field_suspicious_text().fill('tom')
       self.checkNotebookPage.btn_save_suspicious_notebook_popup().click()

   def notebook_suspicion_approved_process(self):
       self.checkNotebookPage.btn_suspicion_approved().click()
       self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_suspicious_reason(),self.checkNotebookPage.dropdown_suspicious_reason_list(),'div')
       self.checkNotebookPage.btn_choose_suspicious_dropdown_options().click()
       self.checkNotebookPage.field_suspicious_text().fill('tom')
       self.checkNotebookPage.btn_save_suspicious_notebook_popup().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def notebook_suspicion_denied_process(self):
       self.checkNotebookPage.btn_suspicion_denied().click()
       self.checkNotebookPage.btn_save_suspicion_denied_popup().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

    # --------------------------- Uncheck Notebook Flows ---------------------------

   def flow_set_uncheck_notebook(self):
       self.checkNotebookPage.btn_uncheck_notebook().click()
       self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_uncheck_reason(),self.checkNotebookPage.dropdown_uncheck_reason_list(),'div')
       self.uncheck_reason = self.functions.get_placeholder_text(self.checkNotebookPage.dropdown_uncheck_reason()).strip()
       self.checkNotebookPage.btn_save_uncheck_notebook_popup().click()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

    # --------------------------- Half Discharge Flow ---------------------------

   def assert_and_perform_half_discharge(self):
       self.functions.check_if_button_enabled_and_click(self.portionPage.btn_half_discharge_loading(),"The half discharged button is not clickable")
       self.portionPage.btn_save_loading_half_discharge_popup().click()
       self.page.reload()
       self.functions.check_row_disabled_soft_assert(self.functions.table_choose_a_row(2),"The Portion is still Enable - The half discharge Action dosent work")



