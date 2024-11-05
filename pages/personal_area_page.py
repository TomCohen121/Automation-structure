from pages.base_page import BasePage
from playwright.sync_api import Page

class PersonalAreaPage(BasePage):
    def __init__(self, page: Page):  # הוספת הסוג של הפרמטר
        super().__init__(page)

    # --------------------------- SideBar Buttons Locators ---------------------------
    def btn_questionnaire_evaluation(self):
        return self.page.get_by_role("button", name="הערכת שאלון")

    def btn_reception_screens(self):
        return self.page.locator('//div[@class="menuItem" and contains(text(), "מסכי קליטה")]')

    def btn_loading_for_the_evaluator(self):
        return self.page.locator('//div[@class="menuItem" and contains(text(), "טעינה למעריך")]')


    # --------------------------- Dashboard Statistics Locators ---------------------------
    def txt_num_of_discharged_loadings(self):
        return self.page.locator('.finished').first.text_content()

    def txt_num_of_discharged_portions(self):
        return self.page.locator('.finished').nth(1).text_content()

    def txt_num_of_discharged_notebooks(self):
        return self.page.locator('.finished').nth(2).text_content()

    def txt_num_of_uncheck_notebooks(self):
        return self.page.locator('.finished').nth(3).text_content()

