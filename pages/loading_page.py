import re
from pages.base_page import BasePage
from playwright.sync_api import Page

class LoadingPage(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)


   def field_search(self, waitBefore=False):
       if waitBefore: self.page.wait_for_selector('input[placeholder="חפש כאן.."]', timeout=1200, state='visible' )
       return self.page.get_by_placeholder("חפש כאן")


   def btn_loading_discharge(self):
       return self.page.get_by_role("button", name="סיום בדיקה ושליחה למרב\"ד")


   def btn_save_loading_discharge_popup(self):
       return self.page.get_by_role("button", name="שמור").click()


   def txt_statistics_number_of_checked_portions(self):
       return self.page.locator("div").filter(has_text=re.compile(r'^מנות שנבדקו \d+$'))


   def txt_statistics_number_of_unchecked_portions(self):
       return self.page.locator("div").filter(has_text=re.compile(r'^מנות שטרם נבדקו \d+$'))


   def txt_statistics_checked_notebooks(self):
       return self.page.locator("div:nth-child(3) > .content").first


   def txt_statistics_unchecked_notebooks(self):
       return self.page.locator("div:nth-child(5) > .content > span").first


   def btn_loading_archive(self):
       return self.page.get_by_role("button", name="מעבר לארכיון טעינות")