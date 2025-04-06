from datetime import date

from assertpy import assert_that
from pytest_playwright.pytest_playwright import page


def test_api(f, add_allure_attach, page):
    """Test function using the generic API request function."""
    url1 = "https://marvad-test.mrvd.education.gov.il:4434/api/NotebookEvaluation/save-and-finish-validation?notebookInLoadingId=53106933"
    data1 = {
        'notebookInLoadingId': 53106933
        }
    response_data = f.functions.make_api_request(url1, data1, "GET", "data")
    assert_that(response_data['value']).is_equal_to("יש לצפות בכל דפי המחברת לפני סיום בדיקת מחברת")
    # -------------------------------------------------------------------------------------------------------
    url2 = "https://marvad-test.mrvd.education.gov.il:4434/api/NotebookEvaluation/page-log"
    notebook_id = 53106933
    total_pages = 4
    results = []
    for page_number in range(2, total_pages + 1):
        data2 = {
            "notebookInLoadingId": notebook_id,
            "pageNumber": page_number,
            "pagesAmount": total_pages
        }
        f.functions.make_api_request(url2, data2, "POST", "data")
    # -------------------------------------------------------------------------------------------------------
    url3 = "https://marvad-test.mrvd.education.gov.il:4434/api/NotebookEvaluation/save-and-finish-validation?notebookInLoadingId=53106933"
    data3 = {
        'notebookInLoadingId': 53106933
        }
    response_data = f.functions.make_api_request(url3, data3, "GET", "data")
    assert_that(response_data['value']).is_equal_to("יש להזין ציון לפחות לשאלה אחת")
    # -------------------------------------------------------------------------------------------------------
    url4 = "https://marvad-test.mrvd.education.gov.il:4434/api/NotebookEvaluation/save/question-grade"
    data4 = {
            "grade": "1",
            "questionId": 767607,
            "notebookInLoadingId": "53106933"
            }
    f.functions.make_api_request(url4, data4, "POST", "data")
    # -------------------------------------------------------------------------------------------------------
    url5 = "https://marvad-test.mrvd.education.gov.il:4434/api/NotebookEvaluation/save-and-finish?notebookInLoadingId=53106933"
    data5 = {
        "notebookInLoadingId": 53106933
            }
    f.functions.make_api_request(url5, data5, "POST", "data")





