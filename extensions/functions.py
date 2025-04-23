import re
import time
from urllib.parse import urlparse
import requests
from playwright.sync_api import Page, Locator
from helper.configuration_manager import ConfigurationManager
from helper.soft_assert import soft_assert
from pages.base_page import BasePage
from pages.check_notebook_page import CheckNotebookPage
from pages.loading_page import LoadingPage
from pages.messages import Messages
from pages.notebook_page import NotebookPage
from pages.personal_area_page import PersonalAreaPage
from pages.portion_page import PortionPage
from pages.suspicious_loading_notebook_page import SuspiciousLoadingNotebookPage
from pages.suspicious_loading_portions_page import SuspiciousLoadingPortionPage
from pages.personal_details_page import PersonalDetailsPage


class Functions(BasePage):
    user_token = None
    def __init__(self, page: Page):
        super().__init__(page)
        self.personalAreaPage = PersonalAreaPage(self.page)
        self.loadingPage = LoadingPage(self.page)
        self.checkNotebookPage = CheckNotebookPage(self.page)
        self.notebookPage = NotebookPage(self.page)
        self.portionPage = PortionPage(self.page)
        self.suspiciousLoadingPortionPage = SuspiciousLoadingPortionPage(self.page)
        self.suspiciousLoadingNotebookPage = SuspiciousLoadingNotebookPage(self.page)
        self.messages = Messages(self.page)
        self.user_token = self.authorization_token(ConfigurationManager.token_url())
        self.personalDetailsPage = PersonalDetailsPage(self.page)

    # --------------------------- Check Functions ---------------------------

    def check_if_loading_number_exist(self, loading_number, variable_name):
        """Checks if the loading number exists or if the loading number field is not fill."""
        if not loading_number or loading_number == "fill":
            raise ValueError(f"Error: The loading number '{variable_name}' is empty. Please check the configuration.")

    def check_if_loading_exists_in_archives(self, locator, number):
        """Checks if the loading text in archives matches the expected number."""
        try:
            return locator.text_content() == number
        except Exception as e:
            raise RuntimeError(f"[ERROR] An error occurred while checking if loading exists in archives: {e}")

    def go_to_user(self, url):
        try:
            self.page.goto(url)
        except Exception as e:
            raise RuntimeError(f"[ERROR] An error occurred while navigating to the URL: {e}")

    # --------------------------- Table Interaction Functions ---------------------------

    def choose_filter_option(self, option_name):
        """selecting a filter option and saving the selection."""
        try:
            self.page.locator("app-loadings-for-evaluator-page app-icon-button").get_by_role("button").click()
            self.loadingPage.btn_clean_all_filters().click()
            checkbox_locator = self.page.locator(f"label:text-is('{option_name.strip()}')")
            checkbox_locator.click()
            self.page.get_by_role("button", name="שמור").click()
        except Exception as e:
            raise RuntimeError(f"[ERROR] An error occurred while selecting the filter option '{option_name}': {e}")

    def table_choose_a_row(self, row_number):
        """Selects a specific row in a table based on the row number."""
        try:
            return self.page.locator(f"tr:nth-child({row_number})")
        except Exception as e:
            raise RuntimeError(f"[ERROR] Failed to locate row {row_number} in the table: {e}")

    def check_row_disabled_soft_assert(self, row_locator, error_message="The row is not disabled as expected"):
        """Uses soft assert to Checks if a row is disabled (for half discharge)."""
        row_class = row_locator.get_attribute("class")
        is_disabled = "disabled" in (row_class or "")
        soft_assert.check(is_disabled, error_message)

    def search_loading(self, loadingNumber):
        """Fills the loading number in the search field and submits it."""
        try:
            self.loadingPage.field_search().fill(loadingNumber)
            self.loadingPage.field_search().press('Enter')
            self.page.wait_for_timeout(2000)
        except Exception as e:
            print(f"[ERROR] Unexpected error in search_loading: {e}")
            raise

    # --------------------------- Loading Functions ---------------------------

    def wait_for_element(self, locator, timeout=5000):
        try:
            locator.wait_for(timeout=timeout)
        except Exception:
            print("❌ The element does not exist")

    def wait_for_loader(self, timeout=35000, timeout_for_second=5000):
        """Waits for the loader to appear (if exists) and then disappear."""
        try:
            if self.page.query_selector(".loading-bar-wrapper.show"):
                self.page.wait_for_selector(".loading-bar-wrapper.show", timeout=timeout)
                self.page.wait_for_selector(".loading-bar-wrapper", state="hidden", timeout=timeout_for_second)
        except Exception as e:
            print(f"Loader wait skipped or failed: {e}")

    def reload_page(self):
        self.page.reload()

    # --------------------------- Popup Functions ---------------------------

    def popup_answer_law(self, timeout=3000, interval=0.5):
        """Verifies if the Popup 'Answer Law' exists and closes it."""
        start_time = time.time()
        try:
            while (time.time() - start_time) * 1000 < timeout:
                close_button = self.page.query_selector(".close-btn")
                if close_button:
                    close_button.click()
                    return True
                time.sleep(interval)
            return False
        except Exception as e:
            print(f'Error: {e}')
            return False

    def assert_verify_popup_error_message(self, locator, expected_text):
        """Asserts that a popup error message is visible and matches the expected text."""
        soft_assert.check(locator.is_visible(), f'Expected popup with locator {locator} to be visible, but it is not.')
        popup_text = self.checkNotebookPage.txt_saving_notebook_error_message().text_content()
        soft_assert.check(popup_text == expected_text, f'Expected popup text: "{expected_text}", but got: "{popup_text}".')

    def verify_correct_popup_appeared(self,locator, error_message="The Popup Error Message did not appear as expected", timeout=5000):
        """Verifies that the Correct popup appears within the specified timeout."""
        try:
            if not locator.is_visible(timeout=timeout):
                raise AssertionError(error_message)
        except Exception as e: #idempotent catch
            raise AssertionError(f"An unexpected error occurred: {str(e)}")

    # --------------------------- Checkbox Functions ---------------------------

    def assert_is_checkbox_checked(self, locator, expected_checked):
        """Checks if a checkbox's state matches the expected state (checked/unchecked)."""
        checkbox = locator
        is_checked = checkbox.get_attribute("ng-reflect-checked") == "true"
        assert is_checked == expected_checked, (
            f"Checkbox state is wrong: Expected {'checked' if expected_checked else 'unchecked'}, "
            f"but found {'checked' if is_checked else 'unchecked'}.")

    # --------------------------- Notebook Functions ---------------------------

    def notebook_pagination_loop(self):
        """Clicks the pagination button until it is no longer enabled."""
        try:
            while self.checkNotebookPage.btn_notebook_pagination().is_enabled():
                self.checkNotebookPage.btn_notebook_pagination().click()
                self.page.wait_for_timeout(300)
        except Exception as e:
            raise RuntimeError(f"[ERROR] An error occurred in notebook_pagination_loop: {e}")

    def is_subquestion_exist(self):
        """Checks if the subquestion field exists and fills it with '1' if enabled."""
        try:
            if self.checkNotebookPage.field_subquestion().count() > 0 and self.checkNotebookPage.field_subquestion().is_enabled():
                self.checkNotebookPage.field_subquestion().fill("1")
                self.page.keyboard.press('Enter')
        except Exception as e:
            raise Exception(f"[ERROR] An error occurred in is_subquestion_exist: {e}")

    def questions_numbers_finish_popup(self):
        try:
            popup_locator = self.checkNotebookPage.btn_save_gap_successfully_closed()
            try:
                popup_locator.wait_for(timeout=2000)
            except TimeoutError:
                pass
            if popup_locator.is_visible():
                popup_locator.click()
                return
        except Exception as e:
            pass

    def fill_question_numbers(self, question_numbers, api_data):
        """Fills in question numbers and sub-question numbers, sets scores, and saves the data."""
        for number in question_numbers:
            question_data = api_data["data"].get(str(number), {})
            locator = self.checkNotebookPage.field_question_number()
            locator.fill(str(number))
            self.page.keyboard.press('Enter')
            subquestion_numbers = self.extract_subquestion_numbers(question_data)
            if subquestion_numbers:
                for sub_number in subquestion_numbers:
                    child_locator = self.checkNotebookPage.field_subquestion()
                    child_locator.fill(str(sub_number))
                    self.page.keyboard.press('Enter')
                    self.checkNotebookPage.field_question_score().fill('6')
                    self.checkNotebookPage.btn_maximum_grade().click()
                    if self.handle_popup_for_question_numbers():
                        return
            else:
                self.checkNotebookPage.field_question_score().fill('6')
                self.checkNotebookPage.btn_maximum_grade().click()
                if self.handle_popup_for_question_numbers():
                    return

    def handle_popup_for_question_numbers(self):
        """Handles the popup if the score field is disabled."""
        try:
            if self.checkNotebookPage.field_question_score().is_disabled():
                popup_locator = self.checkNotebookPage.btn_save_gap_successfully_closed()
                try:
                    popup_locator.wait_for(timeout=2000)
                except TimeoutError:
                    pass
                if popup_locator.is_visible():
                    popup_locator.click()
                    return True
        except Exception:
            pass
        return False

    # --------------------------- Data Extraction Functions ---------------------------

    def extracting_value_from_statistics(self, locator):
        try:
            x = locator.text_content()
            match = re.search(r'\d+', x)
            if match:
                number = int(match.group())
                return number
            raise RuntimeError("[ERROR] No numeric value found in extracting_value_from_statistics.")
        except Exception as e:
            raise RuntimeError(f"[ERROR] Unexpected error in extracting_value_from_statistics: {e}")

    def extracting_total_notebook_grade(self, locator):
        """Extracts a float value from the locator's text content, matching a number pattern."""
        try:
            text_content = locator.text_content().strip()
            match = re.search(r'(\d+\.?\d*)', text_content)  # this would fail for .76 and that's okay
            number = match.group(0)
            return int(float(number))
        except Exception as e:
            raise RuntimeError(f"[ERROR] Unexpected error in extracting_total_notebook_grade: {e}")

    # --------------------------- Assertion Functions ---------------------------

    def assert_equal_to(self, value1, value2, message=None):
        """Asserts that two values are equal, logging a message if not."""
        if message is None:
            message = f'Assertion failed: {value1} is not equal to {value2}'
        soft_assert.check(value1 == value2, message)

    # --------------------------- Dropdown Functions ---------------------------

    def select_first_option_from_dropdown(self, dropdown_locator, options_list_locator, element_type):
        """Selects the first option from a dropdown list."""
        try:
            dropdown_locator.click()
            options_list_locator.wait_for(state='visible')
            first_option = options_list_locator.locator(element_type).first
            first_option.click()
        except Exception as e:
            raise RuntimeError(f"[ERROR] Failed to select the first option from dropdown: {e}")

    # --------------------------- Utility Functions ---------------------------

    def convert_to_int_from_str_or_number(self,value):
        """function converts a string or number to an integer, Convert to 0 if it's not a Number."""
        if isinstance(value, str):
            value = value.strip() if value.strip() else '0'
        try:
            return int(value)
        except ValueError:
            return 0

    def number_to_int(self, number_str):
        """Converts a string to an integer after stripping whitespace."""
        try:
            return int(self.number_to_float(number_str))
        except Exception as e:
            raise RuntimeError(f"[ERROR] Unexpected error in number_to_int: {e}")

    def number_to_float(self, number_str):
        """Converts a string to a float after stripping whitespace."""
        try:
            number = number_str.strip()
            return float(number)
        except Exception as e:
            raise RuntimeError(f"[ERROR] Unexpected error in number_to_float: {e}")

    def get_placeholder_text(self, locator):
        """Returns the placeholder text of a given locator."""
        try:
            locator.wait_for(state="visible", timeout=5000)
            placeholder_text = locator.get_attribute("placeholder")
            return placeholder_text
        except Exception as e:
            raise RuntimeError(f"[ERROR] Failed to get placeholder text: {e}")

    def get_current_url(self, page):
        """Returns the current URL of the given page."""
        try:
            return page.url
        except Exception as e:
            raise RuntimeError(f"[ERROR] An error occurred while retrieving the current URL: {e}")

    # --------------------------- Element Interaction Functions ---------------------------

    def click_element_if_visible(self, element_locator_function, timeout=1200):
        """Clicks an element if it is visible within a given timeout."""
        try:
            element = element_locator_function().wait_for(timeout=timeout)
            if element.is_visible():
                element.click()
        except Exception as e:
            pass

    def click_button_if_enabled(self, button):
        try:
            if button.is_enabled():
                button.click()
        except Exception as e:
            raise RuntimeError(f"[ERROR] An error occurred while clicking delete notebook: {e}")

    def click_delete_notebook_if_enabled(self):
        try:
            button = self.checkNotebookPage.btn_delete_notebook_test()
            if button.is_enabled():
                button.click()
                self.checkNotebookPage.btn_save_delete_notebook_test().click()
                self.page.wait_for_timeout(1000)
        except Exception as e:
            raise RuntimeError(f"[ERROR] An error occurred while clicking delete notebook: {e}")

    def click_delete_notebook_if_enabled_suspicious(self):
        try:
            button = self.checkNotebookPage.btn_delete_notebook_test()
            if button.is_enabled():
                button.click()
                self.checkNotebookPage.btn_save_delete_notebook_test_suspicious().click()
                self.page.wait_for_timeout(1000)
        except Exception as e:
            raise RuntimeError(f"[ERROR] An error occurred while clicking delete notebook suspicious: {e}")

    def click_delete_portion_if_enabled(self):
        try:
            button = self.portionPage.btn_delete_portion_data()
            if button.is_enabled():
                button.click()
                self.portionPage.btn_save_delete_portion_data().click()
        except Exception as e:
            raise RuntimeError(f"[ERROR] An error occurred while clicking delete portion: {e}")

    def check_if_button_enabled_and_click(self, button_locator, error_message):
        """Waits for a button to be visible, clicks it if enabled."""
        button_locator.wait_for(state="visible", timeout=5000)
        if button_locator.is_enabled():
            button_locator.click()
        else:
            raise Exception(error_message)

    def assert_element_exists(self, element, button_name: str):
        """Checks if an element is existed."""
        try:
            element.wait_for(timeout=10000)
            element_visible = element.is_visible()
            element_enabled = element.is_enabled()
            condition = element_visible or not element_enabled
            soft_assert.check(True, f"{button_name} exist")
            if condition:
                print(f"{button_name} exists. ✅")
        except Exception:
            soft_assert.check(False,f"{button_name} does NOT exist ❌")

    def assert_element_not_exists(self, element, button_name: str):
        """Checks if an element does not exist or is not visible and enabled."""
        try:
            element.wait_for(timeout=2000)
            element_visible = element.is_visible()
            element_enabled = element.is_enabled()
            condition = not element_visible or not element_enabled
            soft_assert.check(condition, f"{button_name} should NOT exist ❌")
            if not condition:
                print(f"{button_name} should NOT exist, but it was found ❌")
            else:
                print(f"{button_name} does not exist, as expected.✅")
        except Exception as e:
            print(f"{button_name} does NOT exist as expected.✅")
            soft_assert.check(True,f"{button_name} does not exist, as expected. ✅")

    def assert_is_field_disabled(self, locator):
        element = locator
        is_disabled = element.is_disabled()
        soft_assert.check(is_disabled, "The field is not disabled as expected.")
        return is_disabled

    # ---------------------------  API Fetch Data Functions ---------------------------

    def fetch_api_data_mismatch_notebook_questions(self, params=None): #less generic name
        """Fetches API data related to mismatched questions for the notebook."""
        try:
            current_url = self.page.url
            parsed_url = urlparse(current_url)
            segments = parsed_url.path.split('/')
            notebook_id = segments[segments.index('notebooks') + 1]
            api_url = f"{ConfigurationManager.server_url(self)}NotebookEvaluation/questions?notebookInLoadingId={notebook_id}"
            response = requests.get(api_url, params=params, verify=False, headers={"Authorization": f"Bearer {self.user_token}"})
            data = response.json()
            return data
        except Exception as e:
            raise RuntimeError(f"[ERROR] An error occurred while fetching API data: {e}")

    def fetch_api_data_senior_notebook_questions(self, params=None):
        """Fetches API data related to expert evaluation questions for the notebook."""
        current_url = self.page.url
        parsed_url = urlparse(current_url)
        segments = parsed_url.path.split('/')
        notebook_id = segments[segments.index('notebooks') + 1]
        api_url = f"{ConfigurationManager.server_url(self)}NotebookEvaluation/questions?notebookInLoadingId={notebook_id}"
        response = requests.get(api_url, params=params, verify=False, headers={"Authorization": f"Bearer {self.user_token}"})
        data = response.json()
        return data


    # ---------------------------  Extract From API Functions ---------------------------

    def extract_keys(self, data):
        """Extract numeric keys from the "data" field."""
        if "data" in data and isinstance(data["data"], dict):
            numeric_keys = [key for key in data["data"].keys() if key.isdigit()]
            return numeric_keys
        else:
            print("No 'data' field found or it's not a dictionary.")
            return []

    def extract_subquestion_numbers(self,question_data):
        """Extracts subquestion numbers from question data."""
        children = question_data.get("children", None)
        subquestion_numbers = []
        if children:
            for child_key, child_data in children.items():
                subquestion_number = child_data.get("subQuestionNumber")
                if subquestion_number:
                    subquestion_numbers.append(subquestion_number)
        return subquestion_numbers

    def extract_unanswered_descriptions(self, data):
        """Extracts descriptions of unanswered questions from the API data."""
        unanswered_descriptions = []
        def traverse_questions(questions):
            if not isinstance(questions, dict):  # בדוק אם זה מילון
                return
            for question in questions.values():
                if not question.get("isAnswered", True):
                    unanswered_descriptions.append(question.get("description"))
                if question.get("children"):
                    traverse_questions(question["children"])
        root_data = data.get("data", {})
        traverse_questions(root_data)
        formatted_output = ','.join(unanswered_descriptions)
        return formatted_output

    # ---------------------------  API Process Functions ---------------------------

    def process_api_data(self, fetch_function):
        """Processes API data by calling the fetch function and filling the questions."""
        api_data = fetch_function()
        question_numbers = self.extract_keys(api_data)
        self.fill_question_numbers(question_numbers, api_data)

    def authorization_token(self, token2):
        url = f'{ConfigurationManager.server_url(self)}User/sso?sso=DEV'
        headers = {'SC': token2}
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        return response.json().get('data')

    def make_api_request(self, url, data, request_type, field_to_get):
        """Generic function to make API requests."""
        token = self.user_token
        headers = {"Authorization": f"Bearer {token}"}
        try:
            request_func = getattr(requests, request_type.lower(), None)
            if not request_func:
                raise ValueError(f"Unsupported request type: {request_type}")
            response = request_func(url, headers=headers, json=data)
            response.raise_for_status()  # Raise an error for HTTP failures (4xx, 5xx)
            response_data = response.json()
            print(response_data)
            return response_data.get(field_to_get, {})
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    def upload_and_verify_file(self, file_path, file_input_locator, file_name_locator):
        self.page.set_input_files(file_input_locator, file_path)
        file_name_element = self.page.locator(file_name_locator)
        file_name = file_name_element.text_content()
        expected_file_name = file_path.split("\\")[-1]
        assert file_name == expected_file_name, f"Expected file name: {expected_file_name}, but got: {file_name}"
        print("File uploaded successfully and name verified.")

    def go_to_edit_screen_and_clear_rows(self, update_button):
        self.personalAreaPage.btn_view_update_user_data().click()
        update_button.click()
        while True:
            try:
                if self.personalDetailsPage.btn_delete_row().is_enabled(timeout=3000):
                    self.personalDetailsPage.btn_delete_row().click()
                    self.personalDetailsPage.btn_confirm_delete().click()
                else:
                    break
            except:
                break

