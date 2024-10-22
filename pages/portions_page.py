
from pages.base_page import BasePage
from playwright.sync_api import Page



class PortionPage(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)


   def txt_table_number_of_checked_notebooks(self, row_number):
       text_value = self.page.locator(f"tr:nth-child({row_number}) td:nth-child(9) > .data-wrapper > span").first.text_content()
       return int(text_value.strip())


   def txt_table_avg_grade(self, row_number):
       text_value = self.page.locator(f"tr:nth-child({row_number}) td:nth-child(11) > .text-wrapper > .text-overflow > span").first.text_content()
       return float(text_value)


   def txt_table_portion_status(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number}) td:nth-child(7) > .text-wrapper > .text-overflow > span").first.text_content()


   def btn_half_discharge_loading(self):
       return self.page.get_by_role("button", name="פריקה חלקית")


   def btn_save_loading_half_discharge_popup(self):
       return self.page.get_by_role("button", name="שמור")


