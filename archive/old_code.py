def fill_question_numbers(self, question_numbers, api_data):
    """fills in question numbers and sub-question numbers, sets scores for them, and saves the data."""
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
                try:
                    if self.checkNotebookPage.field_question_score().is_disabled():
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
        else:
            self.checkNotebookPage.field_question_score().fill('6')
            self.checkNotebookPage.btn_maximum_grade().click()
            if self.checkNotebookPage.field_question_score().is_disabled():
                self.checkNotebookPage.btn_save_gap_successfully_closed().wait_for(timeout=2000)
                try:
                    if self.checkNotebookPage.field_question_score().is_disabled():
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
