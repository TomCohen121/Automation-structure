import re
from pages.base_page import BasePage
from playwright.sync_api import Page
from pages.check_notebook_page import CheckNotebookPage
from pages.loading_page import LoadingPage
from pages.notebook_page import NotebookPage
from pages.personal_area_page import PersonalAreaPage
from pages.portions_page import PortionPage


class Functions(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)
       self.personalAreaPage = PersonalAreaPage(self.page)
       self.loadingPage = LoadingPage(self.page)
       self.checkNotebookPage = CheckNotebookPage(self.page)
       self.notebookPage = NotebookPage(self.page)
       self.portionPage = PortionPage(self.page)

   def search_loading(self, loadingNumber):
       self.loadingPage.field_search().fill(loadingNumber)
       self.loadingPage.field_search().press('Enter')


   def popup_answer_law(self):
       close_button = self.page.get_by_role("button", name="סגור")
       if close_button.is_visible():
           self.page.locator("app-small-button").filter(has_text="סגור").click()

   def notebook_pagination_loop(self):
       while self.checkNotebookPage.btn_notebook_pagination().is_enabled():
          self.checkNotebookPage.btn_notebook_pagination().click()


   def is_subquestion_exist(self):
       if self.checkNotebookPage.field_subquestion().count() > 0 and self.checkNotebookPage.field_subquestion().is_enabled():
           self.checkNotebookPage.field_subquestion().fill("1")


   def number_of_checked_portions(self, locator):
       x = locator.text_content()
       match = re.search(r'\d+', x)
       if match:
           number = int(match.group())
           return number