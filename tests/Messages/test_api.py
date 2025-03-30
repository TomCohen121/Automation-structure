import requests
from lxml.html.diff import token
from pytest_playwright.pytest_playwright import page
from assertpy import assert_that
from helper.configuration_manager import ConfigurationManager
from helper.utils import *

# def test_api(f, add_allure_attach, page):
#     url = "https://marvad-test.mrvd.education.gov.il:4434/api/Notebook/save"
#     token = f.functions.user_token
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }
#     data = {
#             "buttonAction": 136,
#             "loadingId": "1805454",
#             "portionInLoadingId": "8274281",
#             "notebookInLoadingId": "45673700"
#     }
#     response = requests.post(url, headers=headers , json=data)
#     response_status = response.status_code
#     response_data = response.json()
#     records = response_data.get("data", {})
#     print(response_status)
#     print(records)
#     print(response_data)



def test_api(f, add_allure_attach, page):
    """Test function using the generic API request function."""
    url = "https://marvad-test.mrvd.education.gov.il:4434/api/Notebook/save"
    data = {
        "buttonAction": 136,
        "loadingId": "1805454",
        "portionInLoadingId": "8274281",
        "notebookInLoadingId": "45673700"
    }
    response_data = f.functions.make_api_request(url, data, "POST", "data")
    if response_data is not None:
        print("Response Data:", response_data)
    else:
        print("Failed to retrieve data.")





