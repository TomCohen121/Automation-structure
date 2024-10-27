from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class CheckNotebookPage(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)


   def field_question_number(self) :
       return self.page.locator('input[name="questionNum"]')


   def field_question_score(self):
       return self.page.locator('input[name="score"]')


   def field_subquestion(self):
       return self.page.locator('input[name="subQuestion"]')


   def btn_save_question_score(self):
       return self.page.get_by_role("button", name="שמור", exact=True)


   def txt_total_notebook_grade(self):
       return self.page.locator(".summary-scores p").first


   def btn_notebook_pagination(self):
       return self.page.locator(".pagination-buttons > app-icon-button:nth-child(3) > .icon-button")


   def btn_save_and_end_notebook_test(self):
       return self.page.get_by_role("button", name="שמור וסיים בדיקת מחברת")


   def btn_save_notebook_popup(self):
       return self.page.get_by_role("button", name="שמור").nth(2)


   def btn_close_after_saving_notebook(self):
        return self.page.get_by_role("button", name="סגור")


   def btn_suspicious_notebook(self):
       return self.page.get_by_role("button", name="מחברת חשודה")


   def btn_not_reviewable_button(self):
       return self.page.get_by_role("button", name="אי בדיקת מחברת")


   def popup_saving_notebook_error_message(self):
       return self.page.locator(".popUp-message-body")

   def txt_saving_notebook_error_message(self):
       return self.page.get_by_role("paragraph")

   def btn_txt_saving_notebook_error_message_close(self):
       return self.page.get_by_role("button", name="סגור")
