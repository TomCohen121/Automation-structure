import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *

@pytest.mark.messages
@allure.story("Wide distribution permissions for Profession")
@allure.description("Sending a message in Wide distribution for Profession - Verifying message receipt in Number of users")
def test_wide_distribution_for_profession(f, add_allure_attach, page):
    f.workflow.send_message_to_recipient("מקצוע כלכלה")




