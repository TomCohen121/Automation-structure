import re
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

   def notebook_checking_process(self):
       """Process of checking a notebook."""
       self.workflow.answer_one_question()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def notebook_checking_process_with_grade(self):
       """Process of checking a notebook and saving the Notebook grade."""
       self.workflow.answer_one_question()
       self.checkNotebookPage.txt_total_notebook_grade().wait_for(state="visible", timeout=5000)
       self.notebook_grade = self.functions.extracting_total_notebook_grade(self.checkNotebookPage.txt_total_notebook_grade())
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def mismatch_notebook_checking_process(self):
       """Process of checking a Mismatch notebook."""
       self.functions.process_api_data(self.functions.fetch_api_data_mismatch)
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def senior_notebook_checking_process(self):
       """Process of checking a Senior notebook."""
       self.functions.process_api_data(self.functions.fetch_api_data_senior)
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def answer_law_questions_loop(self):
        """filling and saving scores for law-related questions 1 to 5."""
        for i in range(1, 6):
            self.checkNotebookPage.field_question_number().fill(str(i))
            self.checkNotebookPage.field_question_number().press('Enter')
            self.checkNotebookPage.field_question_score().fill('6')
            self.checkNotebookPage.btn_maximum_grade().click()

   def answer_one_question(self):
       self.checkNotebookPage.field_question_number().fill('1')
       self.checkNotebookPage.field_question_number().press('Enter')
       self.functions.is_subquestion_exist()
       self.checkNotebookPage.field_question_score().fill('6')
       self.checkNotebookPage.btn_maximum_grade().click()

   def delete_notebook_test(self):
       """Deletes the notebook test if the delete button is enabled."""
       if self.checkNotebookPage.btn_delete_notebook_test().is_enabled():
           self.checkNotebookPage.btn_delete_notebook_test().click()
           self.checkNotebookPage.btn_save_delete_notebook_test().click()

   def assert_check_notebook_score_deleted(self):
       notebook_grade = self.checkNotebookPage.txt_total_notebook_grade().text_content()
       match = re.search(r'\d+', notebook_grade)
       assert not match, f"Notebook grade was not deleted, The Grade is: {notebook_grade}."

   def assert_check_notebook_uncheck_deleted(self):
       self.checkNotebookPage.btn_uncheck_notebook().click()
       uncheck_reason = self.functions.get_placeholder_text(self.checkNotebookPage.dropdown_uncheck_reason())
       assert uncheck_reason== "חפש כאן...", f'The uncheck process was not deleted, The uncheck reason is: {uncheck_reason}'

   # --------------------------- Navigation Flows ---------------------------

   def navigation_from_loading_to_check_notebook_page(self, row_number, row_number1, row_number2):
       self.functions.table_choose_a_row(row_number).dblclick()
       self.functions.table_choose_a_row(row_number1).dblclick()
       self.functions.popup_answer_law()
       self.functions.table_choose_a_row(row_number2).dblclick()

   def navigation_to_loading_screen(self):
       self.personalAreaPage.btn_questionnaire_evaluation().click()
       self.personalAreaPage.btn_reception_screens().click()
       self.personalAreaPage.btn_loading_for_the_evaluator().click()

   def loading_discharge_and_navigate_to_archive(self):
       """Discharge a loading and navigate to archive screen."""
       self.loadingPage.btn_loading_discharge().click()
       self.loadingPage.btn_save_loading_discharge_popup().click()
       self.loadingPage.btn_loading_archive().click()

    # --------------------------- Asserts Error Message Flows ---------------------------

   def assert_and_validate_popup_and_error_messages_regular_loading(self):
       """Validate the correct error message for Regular loading."""
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(), "יש להזין ציון לפחות לשאלה אחת")

   def assert_and_validate_popup_and_error_messages_answer_law(self):
       """Validate the correct error message for Answer Law."""
       self.workflow.answer_law_questions_loop()
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"אין אפשרות לקלוט שאלה - הפרת חוקי מענה!")

   def assert_and_validate_popup_and_error_messages_suspicious_loading(self):
       """Validate the correct error message for Suspicious loading."""
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(), "יש לאשר / לבטל חשד לפני סיום בדיקה")

   def assert_and_validate_popup_and_error_messages_senior_loading(self):
       """Validate the correct error message for Senior loading."""
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(), "יש לסגור את הפער לפני סיום בדיקה")

   def assert_and_validate_popup_and_error_messages_mismatch_loading(self):
       """Validate the correct error message for Mismatch loading."""
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
       self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_suspicious_reason(),self.checkNotebookPage.dropdown_suspicious_reason_list(),'div')
       self.checkNotebookPage.btn_choose_suspicious_dropdown_options().click()
       self.checkNotebookPage.field_suspicious_text().fill('tom')
       self.checkNotebookPage.btn_save_suspicious_notebook_popup().click()

   def notebook_suspicion_approved_process(self):
       self.workflow.flow_set_suspicious_notebook()
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

   def assert_check_notebook_suspicious_deleted(self):
       self.checkNotebookPage.btn_suspicious_notebook().click()
       badge_count = self.page.locator('div.badges-area > app-badge').count()
       assert badge_count == 0, f'Unexpected badges found! {badge_count} badges exist.'
       suspicious_text = self.checkNotebookPage.field_suspicious_text().text_content()
       assert suspicious_text is None or suspicious_text.strip() == "", f'The suspicious text field is not empty, it contains: {suspicious_text}'

   # --------------------------- Uncheck Notebook Flows ---------------------------

   def flow_set_uncheck_notebook_and_save(self):
       self.workflow.flow_set_uncheck_notebook()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def flow_set_uncheck_notebook(self):
       self.checkNotebookPage.btn_uncheck_notebook().click()
       self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_uncheck_reason(),self.checkNotebookPage.dropdown_uncheck_reason_list(), 'div')
       self.uncheck_reason = self.functions.get_placeholder_text(self.checkNotebookPage.dropdown_uncheck_reason()).strip()
       self.checkNotebookPage.btn_save_uncheck_notebook_popup().click()

    # --------------------------- Half Discharge Flow ---------------------------

   def assert_and_perform_half_discharge(self):
       """Performs half discharge on the loading and verifies the action."""
       self.functions.check_if_button_enabled_and_click(self.portionPage.btn_half_discharge_loading(),"The half discharged button is not clickable")
       self.portionPage.btn_save_loading_half_discharge_popup().click()
       self.functions.reload_page()
       self.functions.check_row_disabled_soft_assert(self.functions.table_choose_a_row(2),"The Portion is still Enable - The half discharge Action dosent work")



