from pages.base_page import BasePage
from playwright.sync_api import Page

class SuspiciousLoadingNotebookPage(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)

   def checkbox_notebook_suspicious_approved(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number}) td:nth-child(6) app-checkbox").first

   def checkbox_notebook_suspicious_denied(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number}) td:nth-child(7) app-checkbox").first

   def txt_suspicious_notebook_status(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number}) td:nth-child(8) .text-wrapper .text-overflow span").first.text_content().strip()