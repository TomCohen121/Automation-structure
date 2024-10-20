import re
from pages.base_page import BasePage
from playwright.sync_api import Page, Error
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

   def table_choose_a_row(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number})")


   def search_loading(self, loadingNumber):
       self.loadingPage.field_search().fill(loadingNumber)
       self.loadingPage.field_search().press('Enter')

   def popup_answer_law(self):
       try:
           close_button = self.page.wait_for_selector("app-small-button:has-text('סגור')", timeout=5000)
           if close_button.is_visible():
               close_button.click()
       except Exception as e:
           pass


   def click_element_if_visible(self, element, timeout=12000):
       try:
           x = self.page.wait_for_selector(element, timeout=timeout)
           if x.is_visible():
               x.click()
       except Exception as e:
           pass


   def notebook_pagination_loop(self):
       while self.checkNotebookPage.btn_notebook_pagination().is_enabled():
          self.checkNotebookPage.btn_notebook_pagination().click()


   def is_subquestion_exist(self):
       if self.checkNotebookPage.field_subquestion().count() > 0 and self.checkNotebookPage.field_subquestion().is_enabled():
           self.checkNotebookPage.field_subquestion().fill("1")


   def extracting_value_from_statistics(self, locator):
       x = locator.text_content()
       match = re.search(r'\d+', x)
       if match:
           number = int(match.group())
           return number


   def extracting_total_notebook_grade(self, locator):
       text_content = locator.text_content()
       match = re.search(r'(\d*\.?\d+)', text_content)
       number = match.group(0)
       print(f'The number is {number}')
       return number

   def wait_for_domcontentloaded(self):
       self.page.wait_for_load_state("domcontentloaded")


   def assert_equal_to(self, value1,value2):
       try:
           assert value1 == value2 # This will pass
           print(f'{value1} is equal to {value2}')
           return True
       except:
           print(f'{value1} is not equal to {value2}')
           return False

   def wait_for_loader(self, timeout=25000):
       try:
           self.page.wait_for_selector(".loading-bar-wrapper.show", timeout=timeout)
           self.page.wait_for_selector(".loading-bar-wrapper", timeout=timeout)
       except:
           pass