from pages.base_page import BasePage
from playwright.sync_api import Page

class PersonalDetailsPage(BasePage):
    def __init__(self, page: Page):  # הוספת הסוג של הפרמטר
        super().__init__(page)

    def btn_personal_area_page_sidebar(self):
        return self.page.locator('button:has([data-mat-icon-name="user-cycle"])')

    def btn_add_new_row(self):
        return self.page.locator("app-button-group button").first

    def btn_delete_row(self):
        return self.page.locator('button[style*="--defaultColor: #F54336"]').first

    def btn_confirm_delete(self):
        return self.page.locator('button:has-text("מחק")')

    def btn_save(self):
        return self.page.get_by_role("button", name="שמור")

    def btn_confirm_save(self):
        return self.page.locator('button.small-button:has-text("שמור")').nth(1)

    def field_examiner_phone(self):
        return self.page.locator("app-dynamic-form-field app-text-input input").nth(2)

    def field_examiner_area_code(self):
        return self.page.locator("app-dynamic-form-field app-text-input input").nth(3)

    def btn_update_examiner_phone(self):
        return self.page.locator("button.small-button", has_text="עדכן טלפונים מומחה")

    def btn_update_employment_institutions(self):
        return self.page.locator("button.small-button", has_text="עדכן מוסדות עיסוק")

    def btn_update_degrees(self):
        return self.page.locator("button.small-button", has_text="עדכן תארים")

    def btn_update_training(self):
        return self.page.locator("button.small-button", has_text="עדכן השתלמויות")

    def btn_update_languages(self):
        return self.page.locator("button.small-button", has_text="עדכן שפות")

    def btn_update_attached_certificates(self):
        return self.page.locator("button.small-button", has_text="עדכן אישורים מצורפים")
