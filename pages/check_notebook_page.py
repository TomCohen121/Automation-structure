from pages.base_page import BasePage
from playwright.sync_api import Locator, Page


class CheckNotebookPage(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)


    # --------------------------- Question Component Locators ---------------------------
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

   def btn_maximum_grade(self):
       return self.page.get_by_role("button", name="ציון מקסימלי")

   def btn_save_gap_successfully_closed(self):
       return self.page.locator('mat-dialog-container >> button[mat-dialog-close]')


    # --------------------------- Notebook Page Locators ---------------------------
   def btn_notebook_pagination(self):
       return self.page.locator(".pagination-buttons > app-icon-button:nth-child(3) > .icon-button")


    # --------------------------- End Notebook Review Locators ---------------------------
   def btn_save_and_end_notebook_test(self):
       return self.page.get_by_role("button", name="שמור וסיים בדיקת מחברת")

   def btn_save_notebook_popup(self):
       return self.page.locator("mat-icon[ng-reflect-svg-icon='arrowLeft']")

   def btn_close_after_saving_notebook(self):
        return self.page.get_by_role("button", name="סגור")


    # --------------------------- Suspicious Notebook Locators ---------------------------
   def btn_suspicious_notebook(self):
       return self.page.get_by_role("button", name="מחברת חשודה")

   def checkbox_mark_suspicious_notebook(self):
       return self.page.get_by_label("סמן כמחברת חשודה - חשד הערכה")

   def dropdown_suspicious_reason(self):
       return self.page.locator('input[placeholder="חפש כאן..."]')

   def dropdown_suspicious_reason_list(self):
       return self.page.locator(".options-wrapper")

   def btn_choose_suspicious_dropdown_options(self):
       return self.page.get_by_role("button", name="בחר")

   def field_suspicious_text(self):
       return self.page.locator('.ck-blurred.ck.ck-content.ck-editor__editable.ck-rounded-corners.ck-editor__editable_inline')

   def btn_save_suspicious_notebook_popup(self):
       return self.page.locator("app-big-button").get_by_role("button", name="שמור")


    # --------------------------- Uncheck Notebook Locators ---------------------------
   def btn_uncheck_notebook(self):
       return self.page.get_by_role("button", name="אי בדיקת מחברת")

   def dropdown_uncheck_reason(self):
       return self.page.locator('input[placeholder]')

   def dropdown_uncheck_reason_list(self):
       return self.page.locator(".options-wrapper")

   def btn_save_uncheck_notebook_popup(self):
       return self.page.locator("app-big-button").get_by_role("button", name="שמור")


    # --------------------------- Error Locators ---------------------------
   def popup_saving_notebook_error_message(self):
       return self.page.locator(".popUp-message-body")

   def txt_saving_notebook_error_message(self):
       return self.page.get_by_role("paragraph")

   def btn_txt_saving_notebook_error_message_close(self):
       return self.page.get_by_role("button", name="סגור")


    # --------------------------- Suspicion Notebook Locators ---------------------------
   def btn_suspicion_approved(self):
       return self.page.get_by_role("button", name="אישור חשד")

   def btn_suspicion_denied(self):
       return self.page.get_by_role("button", name="ביטול חשד")

   def btn_save_suspicion_denied_popup(self):
       return self.page.locator("app-small-button[ng-reflect-text='שמור'] button")

