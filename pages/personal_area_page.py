
from pages.base_page import BasePage


class PersonalAreaPage(BasePage):
   def __init__(self, page):
       super().__init__(page)


    # --------------------------- SideBar Buttons Locators ---------------------------
   def btn_questionnaire_evaluation(self):
       return self.page.get_by_role("button", name="הערכת שאלון")

   def btn_reception_screens(self):
       return self.page.locator('//div[@class="menuItem" and contains(text(), "מסכי קליטה")]')

   def btn_loading_for_the_evaluator(self):
       return self.page.locator('//div[@class="menuItem" and contains(text(), "טעינה למעריך")]')