import re
from extensions.functions import Functions
from pages.base_page import BasePage
from playwright.sync_api import Page
from pages.breadcrumbs import Breadcrumbs
from pages.check_notebook_page import CheckNotebookPage
from pages.loading_page import LoadingPage
from pages.notebook_page import NotebookPage
from pages.personal_area_page import PersonalAreaPage
from pages.portion_page import PortionPage
from pages.suspicious_loading_notebook_page import SuspiciousLoadingNotebookPage
from pages.suspicious_loading_portions_page import SuspiciousLoadingPortionPage
from pages.messages import Messages
from helper.decorators import handle_errors

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
       self.breadcrumbs = Breadcrumbs(self.page)
       self.messages = Messages(self.page)

    # --------------------------- Notebooks Checking Process ---------------------------

   def notebook_checking_process(self):
       """Process of checking a notebook."""
       self.answer_one_question("1")
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def notebook_checking_process_with_grade(self):
       """Process of checking a notebook and saving the Notebook grade."""
       self.answer_one_question("1")
       self.checkNotebookPage.txt_total_notebook_grade().wait_for(state="visible", timeout=5000)
       self.page.wait_for_function("document.querySelectorAll('.exam-title.py-1.px-3.ng-star-inserted .d-flex.gap-3 p')[1] && ""document.querySelectorAll('.exam-title.py-1.px-3.ng-star-inserted .d-flex.gap-3 p')[1].textContent.match(/\\d+/)",timeout=5000)
       self.notebook_grade = self.functions.extracting_total_notebook_grade(self.checkNotebookPage.txt_total_notebook_grade())
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def mismatch_notebook_checking_process(self):
       """Process of checking a Mismatch notebook."""
       self.functions.process_api_data(self.functions.fetch_api_data_mismatch_notebook_questions)
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def senior_notebook_checking_process(self):
       """Process of checking a Senior notebook."""
       self.functions.process_api_data(self.functions.fetch_api_data_senior_notebook_questions)
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

   def answer_one_question(self, question_number: str):
       """Answer one Question."""
       self.checkNotebookPage.field_question_number().fill(question_number)
       self.checkNotebookPage.field_question_number().press('Enter')
       self.functions.is_subquestion_exist()
       self.checkNotebookPage.field_question_score().fill('6')
       self.checkNotebookPage.btn_maximum_grade().click()

   # --------------------------- Delete Flows ---------------------------

   def delete_notebook_test(self):
       """Deletes a notebook test by clicking the delete button and confirming the action."""
       self.checkNotebookPage.btn_delete_notebook_test().click()
       self.checkNotebookPage.btn_save_delete_notebook_test().click()
       self.page.wait_for_timeout(1000)

   def delete_portion_data(self):
       """Deletes portion data by clicking the delete button and confirming the action."""
       self.portionPage.btn_delete_portion_data().click()
       self.portionPage.btn_save_delete_portion_data().click()
       self.page.wait_for_timeout(1000)

    # --------------------------- Notebooks Process ---------------------------

   def assert_add_notebook_comment_and_check(self):
       """Adds a comment to the notebook and opens the comments list."""
       self.checkNotebookPage.btn_add_comment().click()
       self.checkNotebookPage.field_comment_text().fill("tom")
       self.checkNotebookPage.btn_save_comment().click()
       self.checkNotebookPage.btn_all_comments().click()
       notebook_comment = self.checkNotebookPage.txt_first_comment()
       assert notebook_comment == "tom"
       self.checkNotebookPage.btn_close_comment().click()
       self.breadcrumbs.btn_breadcrumbs_to_notebooks_page().click()
       self.functions.popup_answer_law()
       self.notebookPage.txt_table_notebook_comment(2).click()
       notebook_table_comment = self.checkNotebookPage.txt_first_comment()
       assert notebook_table_comment == "tom"

   def assert_check_notebook_score_deleted(self):
       """Verifies that the notebook score has been deleted."""
       self.page.wait_for_function("document.querySelector('.summary-scores p') && !document.querySelector('.summary-scores p').textContent.match(/\\d+/)",timeout=5000)
       notebook_grade = self.checkNotebookPage.txt_total_notebook_grade().text_content()
       match = re.search(r'\d+', notebook_grade)
       assert not match, f"Notebook grade was not deleted, The Grade is: {notebook_grade}."

   def assert_check_notebook_uncheck_deleted(self):
       """Verifies that the notebook uncheck process has been deleted."""
       self.checkNotebookPage.btn_uncheck_notebook().click()
       uncheck_reason = self.functions.get_placeholder_text(self.checkNotebookPage.dropdown_uncheck_reason())
       assert uncheck_reason == "חפש כאן...", f'The uncheck process was not deleted, The uncheck reason is: {uncheck_reason}'

   # --------------------------- Navigation Flows ---------------------------
   @handle_errors
   def navigation_from_loading_to_check_notebook_page(self, row_number, row_number1, row_number2):
       """Navigates from the loading screen to the checkNotebookPage by selecting and interacting with table rows."""
       self.functions.table_choose_a_row(row_number).click()
       self.functions.table_choose_a_row(row_number).dblclick()
       self.functions.table_choose_a_row(row_number1).dblclick()
       self.functions.popup_answer_law()
       self.functions.table_choose_a_row(row_number2).dblclick()

   def navigation_to_loading_screen(self):
       """Navigates to the loading screen from the personal area."""
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
       self.checkNotebookPage.popup_saving_notebook_error_message().wait_for(state="visible", timeout=5000)
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.popup_saving_notebook_error_message().wait_for(state="visible", timeout=5000)
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(), "יש להזין ציון לפחות לשאלה אחת")

   def assert_and_validate_popup_and_error_messages_answer_law(self):
       """Validate the correct error message for Answer Law."""
       self.answer_law_questions_loop()
       self.checkNotebookPage.popup_saving_notebook_error_message().wait_for(state="visible", timeout=5000)
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"אין אפשרות לקלוט שאלה - הפרת חוקי מענה!")

   def assert_and_validate_popup_and_error_messages_suspicious_loading(self):
       """Validate the correct error message for Suspicious loading."""
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.popup_saving_notebook_error_message().wait_for(state="visible", timeout=5000)
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.popup_saving_notebook_error_message().wait_for(state="visible", timeout=5000)
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(), "יש לאשר / לבטל חשד לפני סיום בדיקה")

   def assert_and_validate_popup_and_error_messages_senior_loading(self):
       """Validate the correct error message for Senior loading."""
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.popup_saving_notebook_error_message().wait_for(state="visible", timeout=5000)
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.popup_saving_notebook_error_message()
       self.checkNotebookPage.popup_saving_notebook_error_message().wait_for(state="visible", timeout=5000)
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(), "יש לסגור את הפער לפני סיום בדיקה")

   def assert_and_validate_popup_and_error_messages_mismatch_loading(self):
       """Validate the correct error message for Mismatch loading."""
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.popup_saving_notebook_error_message()
       self.functions.verify_correct_popup_appeared(self.checkNotebookPage.popup_saving_notebook_error_message())
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       notebook_data = self.functions.fetch_api_data_mismatch_notebook_questions()
       unanswered_questions = self.functions.extract_unanswered_descriptions(notebook_data)
       print(f"the queistons is {unanswered_questions}")
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.popup_saving_notebook_error_message()
       self.functions.assert_verify_popup_error_message(self.checkNotebookPage.popup_saving_notebook_error_message(), f"לא הוזן ציון לכל השאלות, יש להזין ציון לשאלות: {unanswered_questions}")

    # --------------------------- Suspicious Notebook Flows ---------------------------

   def flow_set_suspicious_notebook(self):
       """Marks the notebook as suspicious."""
       self.checkNotebookPage.btn_suspicious_notebook().click()
       self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_suspicious_reason(),self.checkNotebookPage.dropdown_suspicious_reason_list(),'div')
       self.checkNotebookPage.btn_choose_suspicious_dropdown_options().click()
       self.checkNotebookPage.field_suspicious_text().fill('tom')
       self.checkNotebookPage.btn_save_suspicious_notebook_popup().click()

   def notebook_suspicion_approved_process(self):
       self.checkNotebookPage.btn_suspicion_approved().click()
       badge_count = self.page.locator('div.badges-area > app-badge').count()
       if badge_count == 0:
          self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_suspicious_reason(),self.checkNotebookPage.dropdown_suspicious_reason_list(), 'div')
          self.checkNotebookPage.btn_choose_suspicious_dropdown_options().click()
       else:
            pass
       self.checkNotebookPage.field_suspicious_text().fill('tom')
       self.checkNotebookPage.btn_save_suspicious_notebook_popup().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def notebook_suspicion_denied_process(self):
       """Denies the suspicion process for the notebook and saves it."""
       self.checkNotebookPage.btn_suspicion_denied().click()
       self.checkNotebookPage.btn_save_suspicion_denied_popup().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def assert_check_notebook_suspicious_deleted(self):
       """Asserts that suspicion details are removed from the notebook."""
       self.checkNotebookPage.btn_suspicious_notebook().click()
       badge_count = self.page.locator('div.badges-area > app-badge').count()
       assert badge_count == 0, f'Unexpected badges found! {badge_count} badges exist.'
       suspicious_text = self.checkNotebookPage.field_suspicious_text().text_content()
       assert suspicious_text is None or suspicious_text.strip() == "", f'The suspicious text field is not empty, it contains: {suspicious_text}'

   def assert_check_notebook_approve_suspicious_deleted(self):
       """Asserts that suspicion approval details are removed from the notebook."""
       self.checkNotebookPage.btn_suspicion_approved().click()
       badge_count = self.page.locator('div.badges-area > app-badge').count()
       assert badge_count == 0, f'Unexpected badges found! {badge_count} badges exist.'
       suspicious_text = self.checkNotebookPage.field_suspicious_text().text_content()
       assert suspicious_text is None or suspicious_text.strip() == "", f'The suspicious text field is not empty, it contains: {suspicious_text}'
       self.checkNotebookPage.btn_x_suspicious_notebook_popup().click()

   def assert_remove_suspicion_button(self):
       self.checkNotebookPage.btn_suspicious_notebook().click()
       badge_count = self.page.locator('div.badges-area > app-badge').count()
       if badge_count == 0:
          self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_suspicious_reason(),self.checkNotebookPage.dropdown_suspicious_reason_list(), 'div')
          self.checkNotebookPage.btn_choose_suspicious_dropdown_options().click()
       else:
            pass
       self.checkNotebookPage.field_suspicious_text().fill('tom')
       self.checkNotebookPage.btn_save_suspicious_notebook_popup().click()
       self.checkNotebookPage.btn_suspicious_notebook().click()
       self.checkNotebookPage.btn_remove_suspicion().click()
       self.checkNotebookPage.btn_remove_suspicion_approve().click()
       self.assert_check_notebook_suspicious_deleted()

   # --------------------------- Uncheck Notebook Flows ---------------------------

   def flow_set_uncheck_notebook_and_save(self):
       """Marks the notebook as unchecked and saves the changes."""
       self.flow_set_uncheck_notebook()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible(self.checkNotebookPage.btn_close_after_saving_notebook())

   def flow_set_uncheck_notebook(self):
       """Marks the notebook as unchecked and selects a reason."""
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

    # --------------------------- Notebook Error Flows ---------------------------

   def assert_invalid_question_number_error(self):
       self.checkNotebookPage.field_question_number().fill("20")
       self.checkNotebookPage.field_question_number().press('Enter')
       expected_text = "מס' שאלה לא תקין"
       actual_text = self.checkNotebookPage.txt_error_question_number()
       assert actual_text == expected_text, f"Expected error message '{expected_text}', but got '{actual_text}'"

   def assert_invalid_comment_error(self):
       self.checkNotebookPage.btn_add_comment().click()
       self.checkNotebookPage.btn_save_comment().click()
       expected_text = "עליך להזין תוכן בכתיבת הערה"
       actual_text = self.checkNotebookPage.txt_error_comment()
       assert actual_text == expected_text, f"Expected error message '{expected_text}', but got '{actual_text}'"

   def assert_invalid_grade_score_error(self):
       self.checkNotebookPage.field_question_number().fill("1")
       self.checkNotebookPage.field_question_number().press('Enter')
       self.functions.is_subquestion_exist()
       self.checkNotebookPage.field_question_score().fill('101')
       self.checkNotebookPage.btn_save_question_score().press('Enter')
       expected_text = "ניקוד לא תקין"
       actual_text = self.checkNotebookPage.txt_error_grade_score()
       assert actual_text == expected_text, f"Expected error message '{expected_text}', but got '{actual_text}'"

   def assert_invalid_uncheck_reason_error(self):
       self.checkNotebookPage.btn_uncheck_notebook().click()
       self.checkNotebookPage.btn_save_uncheck_notebook_popup().click()
       locator = self.checkNotebookPage.dropdown_uncheck_reason()
       dropdown_classes = locator.get_attribute("class")
       assert "error" in dropdown_classes, "The uncheck dropdown didn't get an error"

   def assert_invalid_suspicious_reason_error(self):
       self.checkNotebookPage.btn_suspicious_notebook().click()
       self.checkNotebookPage.btn_save_suspicious_notebook_popup().click()
       expected_text = "אנא מלא את השדות"
       actual_text = self.checkNotebookPage.txt_error_suspicious_notebook()
       assert actual_text == expected_text, f"Expected error message '{expected_text}', but got '{actual_text}'"
       self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_suspicious_reason(),self.checkNotebookPage.dropdown_suspicious_reason_list(),'div')
       self.checkNotebookPage.btn_choose_suspicious_dropdown_options().click()
       self.checkNotebookPage.field_suspicious_text().fill('tom')
       self.checkNotebookPage.field_suspicious_text().clear()
       assert actual_text == expected_text, f"Expected error message '{expected_text}', but got '{actual_text}'"

    # --------------------------- Messages Flows ---------------------------

   def send_message_to_recipient(self, recipient_name, header , body):
       self.messages.btn_plus_new_message().click()
       self.messages.dropdown_recipient_selection().fill(recipient_name)
       self.messages.dropdown_recipient_selection().click()
       self.messages.checkbox_choose_recipient(recipient_name)
       self.messages.btn_choose_recipient_dropdown_options().click()
       self.messages.field_message_header().fill(header)
       self.messages.field_message_body().fill(body)
       self.messages.btn_send_message().click()
       self.messages.btn_approve_send_message().click()
       self.messages.btn_close_success_popup().click()

   def assert_message_display_and_content(self, header , body):
       expected_headline = header
       expected_body = body
       expected_sender = "רונה הורוביץ"
       actual_headline = self.messages.txt_incoming_message_headline()
       actual_body = self.messages.txt_incoming_message_body()
       actual_sender = self.messages.txt_incoming_message_sender()
       actual_body = actual_body.replace("\xa0", " ")
       assert expected_sender == actual_sender, f"Expected error message '{expected_sender}', but got '{actual_sender}'"
       assert expected_headline == actual_headline , f"Expected error message '{expected_headline}', but got '{actual_headline}'"
       assert expected_body == actual_body , f"Expected error message '{expected_body}', but got '{actual_body}'"


