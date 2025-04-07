import allure
import pytest
from pytest_playwright.pytest_playwright import page
from tests.Messages_component.users_for_messages import UsersForMessages


@pytest.mark.messages
@allure.story("Wide distribution permissions for Role")
@allure.description("Sending a message in Wide distribution for Role - Verifying message receipt in Number of users")
def test_wide_distribution_for_role(f, add_allure_attach, page):
    f.workflow.send_message_to_recipient("כלל בוחני הערכה חלופית","wide for role header", "wide for role body")
    f.functions.go_to_user(UsersForMessages.role_user)
    f.messages.btn_first_message().click()
    f.workflow.assert_message_display_and_content("wide for role header", "wide for role body")

    f.functions.go_to_user(UsersForMessages.second_role_user)
    f.messages.btn_first_message().click()
    f.workflow.assert_message_display_and_content("wide for role header", "wide for role body")