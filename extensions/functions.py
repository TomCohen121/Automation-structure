import re
from pages.base_page import BasePage
from playwright.sync_api import Page
from pages.check_notebook_page import CheckNotebookPage
from pages.loading_page import LoadingPage
from pages.notebook_page import NotebookPage
from pages.personal_area_page import PersonalAreaPage
from pages.portions_page import PortionPage
from helper.soft_assert import soft_assert


class Functions(BasePage):
   def __init__(self, page: Page):
       super().__init__(page)
       self.personalAreaPage = PersonalAreaPage(self.page)
       self.loadingPage = LoadingPage(self.page)
       self.checkNotebookPage = CheckNotebookPage(self.page)
       self.notebookPage = NotebookPage(self.page)
       self.portionPage = PortionPage(self.page)


   def table_choose_a_row(self, row_number):
       return self.page.locator(f"tr:nth-child({row_number})")


   def search_loading(self, loadingNumber):
       self.loadingPage.field_search().fill(loadingNumber)
       self.loadingPage.field_search().press('Enter')


   def popup_answer_law(self):
       try:
           close_button = self.page.wait_for_selector("app-small-button:has-text('סגור')", timeout=5000)
           if close_button.is_visible():
               close_button.click()
       except Exception as e:
           pass


   def click_element_if_visible_all(self, element_locator_function, timeout=1200):
       try:
           element = element_locator_function().wait_for(timeout=timeout)
           if element.is_visible():
               element.click()
       except Exception as e:
           pass


   # def click_element_if_visible(self, element, timeout=12000):
   #     try:
   #         x = self.page.wait_for_selector(element, timeout=timeout)
   #         if x.is_visible():
   #             x.click()
   #     except Exception as e:
   #         pass


   def notebook_pagination_loop(self):
       while self.checkNotebookPage.btn_notebook_pagination().is_enabled():
          self.checkNotebookPage.btn_notebook_pagination().click()


   def is_subquestion_exist(self):
       if self.checkNotebookPage.field_subquestion().count() > 0 and self.checkNotebookPage.field_subquestion().is_enabled():
           self.checkNotebookPage.field_subquestion().fill("1")


   def extracting_value_from_statistics(self, locator):
       x = locator.text_content()
       match = re.search(r'\d+', x)
       if match:
           number = int(match.group())
           return number


   def extracting_total_notebook_grade(self, locator):
       text_content = locator.text_content()
       match = re.search(r'(\d*\.?\d+)', text_content)
       number = match.group(0)
       return float(number)


   def wait_for_domcontentloaded(self):
       self.page.wait_for_load_state("domcontentloaded")


   def assert_equal_to(self, value1, value2, message=None):
       if message is None:
           message = f'Assertion failed: {value1} is not equal to {value2}'
       soft_assert.check(value1 == value2, message)


   def wait_for_loader(self, timeout=25000):
       try:
           self.page.wait_for_selector(".loading-bar-wrapper.show", timeout=timeout)
           self.page.wait_for_selector(".loading-bar-wrapper", timeout=timeout)
       except:
           pass


   def check_if_loading_exists_in_archives(self, locator,number):
       return locator.text_content() == number


   def assert_verify_popup_error_message(self, locator, expected_text):
       soft_assert.check(locator.is_visible(), f'Expected popup with locator {locator} to be visible, but it is not.')
       popup_text = self.checkNotebookPage.txt_saving_notebook_error_message().text_content()
       soft_assert.check(popup_text == expected_text,f' Expected popup text: "{expected_text}", but got: "{popup_text}".')


   def select_first_option_from_dropdown(self, dropdown_locator, options_list_locator):
       dropdown_locator.click()
       options_list_locator.wait_for(state='visible')
       first_option = options_list_locator.locator('div').first
       first_option.click()

   def checkbox_is_checked(self, checkbox_locator, expected_state):
       checkbox_locator.wait_for(state="visible")
       is_checked = checkbox_locator.is_checked()
       soft_assert.check(
           is_checked == expected_state,
           f"The Suspicious CheckBox is expected to be {'checked' if expected_state else 'unchecked'}, "
           f"but it is {'checked' if is_checked else 'unchecked'}.")
