import allure
import pytest
from pytest_playwright.pytest_playwright import page
from tests.Messages.users import UsersForMessages


@pytest.mark.messages
@allure.story("Private distribution permissions for Profession and Role")
@allure.description("Sending a message in Private distribution for Profession and Role - Verifying message receipt")
def test_private_distribution_for_role_and_profession(f, add_allure_attach, page):
    f.workflow.send_message_to_recipient("סימה פומרניץ" ,"private role and profession header", "private role and profession body")
    f.functions.go_to_user(UsersForMessages.role_and_profession_user)
    f.messages.btn_first_message().click()
    f.workflow.assert_message_display_and_content("private role and profession header", "private role and profession body")