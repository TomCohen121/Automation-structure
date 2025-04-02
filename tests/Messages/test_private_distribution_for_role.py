import allure
import pytest
from pytest_playwright.pytest_playwright import page
from Messages.users import UsersForMessages


@pytest.mark.messages
@allure.story("Private distribution permissions for Role")
@allure.description("Sending a message in Private distribution for Role - Verifying message receipt")
def test_private_distribution_for_role(f, add_allure_attach, page):
    f.workflow.send_message_to_recipient("רים אבו שריקי","private role header", "private role body")
    f.functions.go_to_user(UsersForMessages.role_user)
    f.messages.btn_first_message().click()
    f.workflow.assert_message_display_and_content("private role header", "private role body")