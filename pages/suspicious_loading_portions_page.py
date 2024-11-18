from pages.base_page import BasePage
from playwright.sync_api import Page



class SuspiciousLoadingPortionPage(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)

    # --------------------------- Variables from Table Locators ---------------------------
   def txt_table_num_of_suspicion_approved(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number}) td:nth-child(10) > .data-wrapper > span").first.text_content()

   def txt_table_num_of_suspicion_denied(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number}) td:nth-child(9) > .data-wrapper > span").first.text_content()

   def txt_table_sus_portion_status(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number}) td:nth-child(7) > .text-wrapper > .text-overflow > span").first.text_content().strip()