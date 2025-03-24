import time

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
       return self.page.locator(".exam-title.py-1.px-3.ng-star-inserted .d-flex.gap-3 p").nth(1)

   def btn_maximum_grade(self):
       return self.page.get_by_role("button", name="ציון מקסימלי")

   def btn_save_gap_successfully_closed(self):
       return self.page.get_by_role("button", name="סגור")

   def btn_senior_total_gap(self):
       time.sleep(3)
       return self.page.locator("app-badge").first.text_content()

    # --------------------------- Notebook Page Locators ---------------------------
   def btn_notebook_pagination(self):
       return self.page.locator("app-notebook-pager").get_by_role("button").nth(1)

   def btn_delete_notebook_test(self):
       return self.page.get_by_role("button", name="מחק בדיקת מחברת")

   def btn_save_delete_notebook_test(self):
       return self.page.get_by_role("button", name="שמור").nth(2)

   def btn_save_delete_notebook_test_suspicious(self):
       return self.page.get_by_role("button", name="שמור").nth(1)

   def btn_add_comment(self):
       return self.page.get_by_role("button", name="הוסף הערה")

   def btn_all_comments(self):
       return self.page.get_by_role("button", name="צפה בכל ההערות")

   def field_comment_text(self):
       return self.page.get_by_placeholder("הקלד את הטקסט שלך כאן...")

   def btn_save_comment(self):
       return self.page.locator("app-big-button").get_by_role("button", name="שמור")

   def txt_first_comment(self):
       return self.page.locator(".text-side p").first.text_content().strip()

   def btn_close_comment(self):
       return self.page.get_by_role("button", name="סגור")

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

   def dropdown_suspicious_reason(self):
       return self.page.locator('input[placeholder="חפש כאן..."]')

   def dropdown_suspicious_reason_list(self):
       return self.page.locator(".options-wrapper")

   def btn_choose_suspicious_dropdown_options(self):
       return self.page.get_by_role("button", name="בחר")

   def field_suspicious_text(self):
       return self.page.locator("quill-editor div").nth(2)

   def btn_save_suspicious_notebook_popup(self):
       return self.page.locator("app-big-button").get_by_role("button", name="שמור")

   def btn_x_suspicious_notebook_popup(self):
       return self.page.locator(".closeSuspiciousNotebookPopup > .mat-icon > svg")

    # --------------------------- Uncheck Notebook Locators ---------------------------

   def btn_uncheck_notebook(self):
       return self.page.get_by_role("button", name="אי בדיקת מחברת")

   def dropdown_uncheck_reason(self):
       return self.page.locator('input[placeholder]')

   def dropdown_uncheck_reason_list(self):
       return self.page.locator(".options-wrapper")

   def btn_save_uncheck_notebook_popup(self):
       return self.page.locator("app-big-button").get_by_role("button", name="שמור")

   def btn_x_uncheck_notebook_popup(self):
       return self.page.locator(".closeRequiredUnableToCheckPopup > .mat-icon > svg")

    # --------------------------- Error Locators ---------------------------
   def popup_saving_notebook_error_message(self):
       return self.page.locator(".mdc-dialog__container")

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

   def txt_approve_and_denied_tag(self):
       return self.page.locator("app-message-bar-square-row")

   def btn_remove_suspicion(self):
       return self.page.get_by_role("button", name="הסר חשד")

   def btn_remove_suspicion_approve(self):
       return self.page.get_by_role("button", name="אישור")


    # --------------------------- Alerts Component Locators ---------------------------
   def txt_error_question_number(self):
       return self.page.locator("div.error").nth(0).text_content().strip()

   def txt_error_grade_score(self):
       return self.page.locator("div.error").nth(2).text_content().strip()

   def txt_error_comment(self):
       return self.page.locator("app-message-bar-row p").text_content().strip()

   def txt_error_suspicious_notebook(self):
       return self.page.locator(".message-bar-row-wrapper.ng-star-inserted p").text_content().strip()