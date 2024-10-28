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
       return self.page.get_by_role("button", name="שמור")


   def txt_statistics_number_of_checked_portions(self):
       return self.page.locator("div").filter(has_text=re.compile(r'^מנות שנבדקו \d+$'))


   def txt_statistics_number_of_unchecked_portions(self):
       return self.page.locator("div").filter(has_text=re.compile(r'^מנות שטרם נבדקו \d+$'))


   def txt_statistics_number_of_nocheck_portions(self):
       return self.page.locator("div").filter(has_text=re.compile(r'^מנות באי בדיקה \d+$'))


   def txt_statistics_checked_notebooks(self):
       return self.page.locator("div:nth-child(3) > .content").first


   def txt_statistics_nocheck_notebooks(self):
       return self.page.locator("div:nth-child(2) > .content").first


   def txt_statistics_suspicious_notebooks(self):
       return self.page.locator("div:nth-child(4) > .content > span").first


   def txt_statistics_unchecked_notebooks(self):
       return self.page.locator("div:nth-child(5) > .content > span").first


   def btn_loading_archive(self):
       return self.page.get_by_role("button", name="מעבר לארכיון טעינות")


   def btn_filter(self):
       return self.page.get_by_role("main").locator("app-icon-button").get_by_role("button")


   def btn_filter_navigation_arrows(self):
       return self.page.locator("div:nth-child(3) > app-svg-icon > .mat-icon > svg")


   def checkbox_loading_moved_to_evaluation(self):
       return self.page.get_by_label("טעינה הועברה למעריך")

   def btn_filter_saving(self):
       return self.page.get_by_role("button", name="שמור")


