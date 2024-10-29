from extensions.functions import Functions
from pages.base_page import BasePage
from playwright.sync_api import Page
from pages.check_notebook_page import CheckNotebookPage
from pages.loading_page import LoadingPage
from pages.notebook_page import NotebookPage
from pages.personal_area_page import PersonalAreaPage
from pages.portions_page import PortionPage

class WorkFlow(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)
       self.personalAreaPage = PersonalAreaPage(self.page)
       self.loadingPage = LoadingPage(self.page)
       self.checkNotebookPage = CheckNotebookPage(self.page)
       self.notebookPage = NotebookPage(self.page)
       self.portionPage = PortionPage(self.page)
       self.functions = Functions(self.page)


   def navigation_to_loading_screen(self):
       self.personalAreaPage.btn_questionnaire_evaluation().click()
       self.personalAreaPage.btn_reception_screens().click()
       self.personalAreaPage.btn_loading_for_the_evaluator().click()


   def notebook_checking_process_with_grade(self):
       self.checkNotebookPage.field_question_number().fill('1')
       self.functions.is_subquestion_exist()
       self.checkNotebookPage.field_question_score().fill('1')
       self.checkNotebookPage.btn_save_question_score().click()
       self.checkNotebookPage.txt_total_notebook_grade().wait_for()
       self.notebook_grade = self.functions.extracting_total_notebook_grade(self.checkNotebookPage.txt_total_notebook_grade())
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible_all(self.checkNotebookPage.btn_close_after_saving_notebook())
       self.functions.wait_for_domcontentloaded()


   def notebook_checking_process(self):
       self.checkNotebookPage.field_question_number().fill('1')
       self.functions.is_subquestion_exist()
       self.checkNotebookPage.field_question_score().fill('1')
       self.checkNotebookPage.btn_save_question_score().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible_all(self.checkNotebookPage.btn_close_after_saving_notebook())
       self.functions.wait_for_domcontentloaded()


   def loading_discharge_and_navigate_to_archive(self):
       self.loadingPage.btn_loading_discharge().click()
       self.loadingPage.btn_save_loading_discharge_popup().click()
       # self.page.get_by_role("button", name="סגור").click()
       self.loadingPage.btn_loading_archive().click()


   def filters_new_loading_search(self):
       self.loadingPage.btn_filter().click()
       self.loadingPage.btn_filter_navigation_arrows().click()
       self.loadingPage.btn_filter_navigation_arrows().click()
       self.loadingPage.btn_filter_navigation_arrows().click()
       self.loadingPage.checkbox_loading_moved_to_evaluation().check()
       self.loadingPage.btn_filter_saving().click()


   def flow_from_loading_to_checknotebookpage(self,row_number,row_number1,row_number2):
       self.functions.table_choose_a_row(row_number).dblclick()
       self.functions.table_choose_a_row(row_number1).dblclick()
       self.functions.table_choose_a_row(row_number2).dblclick()


   def assert_and_validate_popup_and_error_messages(self):
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.assert_verify_popup_error_message(
       self.checkNotebookPage.popup_saving_notebook_error_message(),"יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
       self.checkNotebookPage.btn_txt_saving_notebook_error_message_close().click()
       self.functions.notebook_pagination_loop()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.functions.assert_verify_popup_error_message(
       self.checkNotebookPage.popup_saving_notebook_error_message(), "יש להזין ציון לפחות לשאלה אחת")


   def flow_set_suspicious_notebook(self):
       self.checkNotebookPage.btn_suspicious_notebook().click()
       self.checkNotebookPage.checkbox_mark_suspicious_notebook().check()
       self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_suspicious_reason(),self.checkNotebookPage.dropdown_suspicious_reason_list(),'div')
       self.checkNotebookPage.btn_choose_suspicious_dropdown_options().click()
       self.checkNotebookPage.field_suspicious_text().fill('tom')
       self.checkNotebookPage.btn_save_suspicious_notebook_popup().click()

   def flow_set_uncheck_notebook(self):
       self.checkNotebookPage.btn_uncheck_notebook().click()
       self.functions.select_first_option_from_dropdown(self.checkNotebookPage.dropdown_uncheck_reason(),self.checkNotebookPage.dropdown_uncheck_reason_list(),'div')
       self.uncheck_reason = self.functions.get_placeholder_text(self.checkNotebookPage.dropdown_uncheck_reason()).strip()
       self.checkNotebookPage.btn_save_uncheck_notebook_popup().click()
       self.checkNotebookPage.btn_save_and_end_notebook_test().click()
       self.checkNotebookPage.btn_save_notebook_popup().click()
       self.functions.wait_for_loader()
       self.functions.click_element_if_visible_all(self.checkNotebookPage.btn_close_after_saving_notebook())
       self.functions.wait_for_domcontentloaded()