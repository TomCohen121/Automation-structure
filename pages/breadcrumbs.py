from pages.base_page import BasePage
from playwright.sync_api import Page

class Breadcrumbs(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)

    # --------------------------- Breadcrumbs Buttons Locators ---------------------------
   def btn_breadcrumbs_to_loadings_page(self):
       return self.page.locator("div.label.router-link-active", has_text="טעינות למעריך")

   def btn_breadcrumbs_to_portions_page(self):
       return self.page.locator("div.label.router-link-active", has_text="מנות למעריך")

   def btn_breadcrumbs_to_personal_area_page(self):
       return self.page.locator("div.label.router-link-active", has_text="איזור אישי")

   def btn_breadcrumbs_to_notebooks_page(self):
       return self.page.locator("div.label.router-link-active", has_text="מחברות במנה")