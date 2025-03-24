import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *

@pytest.mark.messages
@allure.story("Private distribution permissions for Profession")
@allure.description("Sending a message in Private distribution for Profession - Verifying message receipt")
def test_private_distribution_for_profession(f, add_allure_attach, page):
    f.workflow.send_message_to_recipient("שאדי ")
    f.goto("https://djmgx4dl196h1.cloudfront.net/dashboard?f5=ZjVTU089ZjVTU091c2VyPTAyOTk0NTc2MyZmNVNTT3Bhc3N3b3JkPTEyMzQ1Njc4")
    f.messages.btn_first_message().click()
    f.workflow.assert_message_display_and_content()


