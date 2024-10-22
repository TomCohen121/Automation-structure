from pages.base_page import BasePage
from playwright.sync_api import Page

class Breadcrumbs(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)

   def btn_breadcrumbs_to_loadings_page(self):
       return self.page.locator("div.label.router-link-active", has_text="טעינות למעריך")


   def btn_breadcrumbs_to_portions_page(self):
       return self.page.locator("div.label.router-link-active", has_text="מנות למעריך")