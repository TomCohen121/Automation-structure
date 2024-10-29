from pages.base_page import BasePage
from playwright.sync_api import Page


class NotebookPage(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)

    # --------------------------- Variables from Table Locators ---------------------------
   def txt_table_number_of_checked_questions(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number}) td:nth-child(4) > .text-wrapper > .text-overflow > span").first.text_content()

   def txt_table_notebook_grade(self, row_number):
       return self.page.locator('td .progress-bar-component p.ng-star-inserted').text_content()

   def txt_table_notebook_status(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number}) td:nth-child(7) > .text-wrapper > .text-overflow > span").first.text_content()

   def checkbox_notebook_suspicious_evaluation(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number}) td:nth-child(5) .mdc-checkbox__native-control").first







