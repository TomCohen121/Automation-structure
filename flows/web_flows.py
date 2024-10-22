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


   def notebook_checking_process(self):
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
       self.functions.click_element_if_visible('button[role="button"][name="סגור"]')
       self.functions.wait_for_domcontentloaded()


   def loading_discharge_and_navigate_to_archive(self):
       self.loadingPage.btn_loading_discharge().click()
       self.loadingPage.btn_save_loading_discharge_popup().click()
       self.page.get_by_role("button", name="סגור").click()
       self.loadingPage.btn_loading_archive().click()
