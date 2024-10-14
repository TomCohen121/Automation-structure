import re
from pages.base_page import BasePage
from playwright.sync_api import Page



class Functions(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)
       self.page = page
       self.initialize = BasePage.initialize_all_pages(page)





   def search_loading(self, loadingNumber):
       # self.loadingPage.field_search().fill(loadingNumber)

       #Use this way !!!
       self.initialize['Functions'].goto_homepage()
       ####

       # self.loadingPage.field_search().press('Enter')
       #Example for fetching the Functions from the global object
       # self.basepageAll.


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




   def number_of_checked_portions(self):
       x = self.page.locator("div").filter(has_text=re.compile(r'^מנות שנבדקו \d+$')).text_content()
       match = re.search(r'\d+', x)
       if match:
           number = int(match.group())
           return number