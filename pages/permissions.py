from pages.base_page import BasePage
from playwright.sync_api import Page

class Permissions(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)

    # --------------------------- Dashboard Page Locators ---------------------------
   def comp_personal_details(self):
       return self.page.locator(".title-page-data.ng-star-inserted")

   def comp_total_evaluations_in_the_last_session(self):
       return self.page.locator(".d-flex.gap-5.align-items-center")

   def comp_evaluation_status(self):
       return self.page.locator(".title:has-text('סטטוס הערכות')")

   def comp_general_info_for_session(self):
       return self.page.locator(".title:has-text('נתונים כלליים למועד')")

   def comp_links(self):
       return self.page.locator(".links-container")

    # --------------------------- Loading Page Locators ---------------------------
   def btn_loading_discharge(self):
       return self.page.get_by_role("button", name="סיום בדיקה ושליחה למרב\"ד")

   def btn_loading_archive(self):
       return self.page.get_by_role("button", name="מעבר לארכיון טעינות")

   def btn_reset_loading_to_starting_state(self):
       return self.page.get_by_role("button", name="החזר טעינה למצב התחלתי")

    # --------------------------- Portion Page Locators ---------------------------
   def btn_half_discharge_loading(self):
       return self.page.get_by_role("button", name="פריקה חלקית")

   def btn_delete_all_evaluations(self):
       return self.page.get_by_role("button", name="מחק כלל הערכות במנה")

   def btn_confirm_no_check(self):
       return self.page.get_by_role("button", name="בטל אי בדיקה")

   def btn_cancel_no_check(self):
       return self.page.get_by_role("button", name="אשר אי בדיקה")

   # --------------------------- Notebook Page Locators ---------------------------
   def btn_delete_notebook_evaluation(self):
       return self.page.get_by_role("button", name="מחק בדיקת מחברת")

   def btn_end_notebook_evaluation(self):
       return self.page.get_by_role("button", name="סיים בדיקת מנה")

   # --------------------------- CheckNotebook Page Locators ---------------------------
   def btn_delete_notebook_evaluation_check_notebook(self):
       return self.page.get_by_role("button", name="מחק בדיקת מחברת")

   def btn_student_adaptations(self):
       return self.page.get_by_role("button", name="התאמות לתלמיד")

   def btn_show_formats(self):
       return self.page.get_by_role("button", name="הצג פורמטים")

   def btn_suspicious_notebook(self):
       return self.page.get_by_role("button", name="מחברת חשודה")

   def btn_uncheck_notebook(self):
       return self.page.get_by_role("button", name="אי בדיקת מחברת")

   def btn_save_and_end_notebook_test(self):
       return self.page.get_by_role("button", name="שמור וסיים בדיקת מחברת")

   def btn_watch_all_comments(self):
       return self.page.locator("//span[contains(text(),'צפה בכל ההערות')]")

   def btn_add_comment(self):
       return self.page.locator('#Outline\\/message\\/24')

   def btn_add_screen(self):
       return self.page.locator("button:has-text('הוספת מסך')")

   def btn_save_question_score(self):
       return self.page.get_by_role("button", name="שמור", exact=True)

   def btn_suspicious_history(self):
       return self.page.locator("button:has-text('הסטוריית חשד')")
