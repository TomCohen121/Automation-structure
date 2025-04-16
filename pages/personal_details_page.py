from pages.base_page import BasePage
from playwright.sync_api import Page

class PersonalDetailsPage(BasePage):
    def __init__(self, page: Page):  # הוספת הסוג של הפרמטר
        super().__init__(page)

    def rol_examiner_phone(self):
        return self.page.locator("div.label.ng-star-inserted", has_text="טלפונים מומחה")

    def btn_update_examiner_phone(self):
        return self.page.locator("button.small-button", has_text="עדכן טלפונים מומחה")

    def btn_add_new_examiner_phone(self):
        return self.page.locator("app-button-group button").first

    def field_examiner_phone(self):
        return self.page.locator("app-dynamic-form-field app-text-input input").nth(2)

    def field_examiner_area_code(self):
        return self.page.locator("app-dynamic-form-field app-text-input input").nth(3)

    def btn_save_new_phone(self):
        return self.page.get_by_role("button", name="שמור")