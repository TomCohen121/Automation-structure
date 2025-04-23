import allure
import pytest
from pytest_playwright.pytest_playwright import page
from tests.Messages_component.users_for_messages import UsersForMessages


@pytest.mark.messages
@allure.story("Wide distribution permissions for Profession")
@allure.description("Sending a message in Wide distribution for Profession - Verifying message receipt in Number of users")
def test_wide_distribution_for_profession(f, add_allure_attach, page):
    f.workflow.send_message_to_recipient("מקצוע כלכלה","wide for profession header", "wide for profession body")
    f.functions.go_to_user(UsersForMessages.get_user_url("profession_user"))
    f.messages.btn_first_message().click()
    f.workflow.assert_message_display_and_content("wide for profession header", "wide for profession body")

    f.functions.go_to_user(UsersForMessages.get_user_url("second_profession_user"))
    f.messages.btn_first_message().click()
    f.workflow.assert_message_display_and_content("wide for profession header", "wide for profession body")
