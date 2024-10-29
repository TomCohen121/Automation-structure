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
        # Initialize page objects
        self.personalAreaPage = PersonalAreaPage(self.page)
        self.loadingPage = LoadingPage(self.page)
        self.checkNotebookPage = CheckNotebookPage(self.page)
        self.notebookPage = NotebookPage(self.page)
        self.portionPage = PortionPage(self.page)

    # --------------------------- Table Interaction Functions ---------------------------

    def table_choose_a_row(self, row_number):
        """Selects a specific row in a table based on the row number."""
        return self.page.locator(f"tr:nth-child({row_number})")

    # --------------------------- Loading Functions ---------------------------

    def search_loading(self, loadingNumber):
        """Fills the loading number in the search field and submits it."""
        self.loadingPage.field_search().fill(loadingNumber)
        self.loadingPage.field_search().press('Enter')

    def wait_for_domcontentloaded(self):
        """Waits for the DOM content to be fully loaded."""
        self.page.wait_for_load_state("domcontentloaded")

    def wait_for_loader(self, timeout=25000):
        """Waits for the loading bar to show and then hide."""
        try:
            self.page.wait_for_selector(".loading-bar-wrapper.show", timeout=timeout)
            self.page.wait_for_selector(".loading-bar-wrapper", timeout=timeout)
        except:
            pass

    def check_if_loading_exists_in_archives(self, locator, number):
        """Checks if the loading text in archives matches the expected number."""
        return locator.text_content() == number

    # --------------------------- Popup Functions ---------------------------

    def popup_answer_law(self):
        """Closes the popup if the close button is visible."""
        try:
            close_button = self.page.wait_for_selector("app-small-button:has-text('סגור')", timeout=5000)
            if close_button.is_visible():
                close_button.click()
        except Exception as e:
            pass

    def assert_verify_popup_error_message(self, locator, expected_text):
        """Asserts that a popup error message is visible and matches the expected text."""
        soft_assert.check(locator.is_visible(), f'Expected popup with locator {locator} to be visible, but it is not.')
        popup_text = self.checkNotebookPage.txt_saving_notebook_error_message().text_content()
        soft_assert.check(popup_text == expected_text, f'Expected popup text: "{expected_text}", but got: "{popup_text}".')

    # --------------------------- Checkbox Functions ---------------------------

    def checkbox_is_checked(self, checkbox_locator, expected_state):
        """Checks if a checkbox's state matches the expected state (checked/unchecked)."""
        checkbox_locator.wait_for(state="visible")
        is_checked = checkbox_locator.is_checked()
        soft_assert.check(
            is_checked == expected_state,
            f"The Suspicious CheckBox is expected to be {'checked' if expected_state else 'unchecked'}, "
            f"but it is {'checked' if is_checked else 'unchecked'}."
        )

    # --------------------------- Notebook Functions ---------------------------

    def notebook_pagination_loop(self):
        """Clicks the pagination button until it is no longer enabled."""
        while self.checkNotebookPage.btn_notebook_pagination().is_enabled():
            self.checkNotebookPage.btn_notebook_pagination().click()

    def is_subquestion_exist(self):
        """Checks if the subquestion field exists and fills it with '1' if enabled."""
        if self.checkNotebookPage.field_subquestion().count() > 0 and self.checkNotebookPage.field_subquestion().is_enabled():
            self.checkNotebookPage.field_subquestion().fill("1")

    # --------------------------- Data Extraction Functions ---------------------------

    def extracting_value_from_statistics(self, locator):
        """Extracts a numeric value from a locator's text content."""
        x = locator.text_content()
        match = re.search(r'\d+', x)
        if match:
            number = int(match.group())
            return number

    def extracting_total_notebook_grade(self, locator):
        """Extracts a float value from the locator's text content, matching a number pattern."""
        text_content = locator.text_content()
        match = re.search(r'(\d*\.?\d+)', text_content)
        number = match.group(0)
        return float(number)

    # --------------------------- Assertion Functions ---------------------------

    def assert_equal_to(self, value1, value2, message=None):
        """Asserts that two values are equal, logging a message if not."""
        if message is None:
            message = f'Assertion failed: {value1} is not equal to {value2}'
        soft_assert.check(value1 == value2, message)

    # --------------------------- Dropdown Functions ---------------------------

    def select_first_option_from_dropdown(self, dropdown_locator, options_list_locator, element_type):
        """Selects the first option from a dropdown list."""
        dropdown_locator.click()
        options_list_locator.wait_for(state='visible')
        first_option = options_list_locator.locator(element_type).first
        first_option.click()

    # --------------------------- Utility Functions ---------------------------

    def number_to_int(self, number_str):
        """Converts a string to an integer after stripping whitespace."""
        number = number_str.strip()
        number_int = int(number)
        return number_int

    def number_to_float(self, number_str):
        """Converts a string to a float after stripping whitespace."""
        number = number_str.strip()
        number_float = float(number)
        return number_float

    def get_placeholder_text(self, locator):
        """Returns the placeholder text of a given locator."""
        locator.wait_for(state="visible", timeout=5000)
        placeholder_text = locator.get_attribute("placeholder")
        return placeholder_text

    # --------------------------- Element Interaction Functions ---------------------------

    def click_element_if_visible_all(self, element_locator_function, timeout=1200):
        """Clicks an element if it is visible within a given timeout."""
        try:
            element = element_locator_function().wait_for(timeout=timeout)
            if element.is_visible():
                element.click()
        except Exception as e:
            pass
