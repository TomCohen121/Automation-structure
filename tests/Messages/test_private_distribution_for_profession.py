import allure
import pytest
from pytest_playwright.pytest_playwright import page
from tests.Messages.users import UsersForMessages


@pytest.mark.messages
@allure.story("Private distribution permissions for Profession")
@allure.description("Sending a message in Private distribution for Profession - Verifying message receipt")
def test_private_distribution_for_profession(f, add_allure_attach, page):
    f.workflow.send_message_to_recipient("איתן ישראלי","private profession header", "private profession body")
    f.functions.go_to_user(UsersForMessages.profession_user)
    f.messages.btn_first_message().click()
    f.workflow.assert_message_display_and_content("private profession header", "private profession body")


