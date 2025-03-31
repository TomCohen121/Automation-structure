import allure
import pytest
from pytest_playwright.pytest_playwright import page


@pytest.mark.dashboard #C18163
@allure.story("Click on Move to Archive or Loadings Button")
@allure.description("Click on Move to Archive Button or the Loadings button - navigate to Archive screen OR user Details page")
def test_move_to_loadings_or_archive(f, add_allure_attach, page):
    #Dashboard
    with f.page.expect_navigation():
        f.personalAreaPage.btn_watch_loadings_move_to_archive().click()
    assert f.page.url.endswith("archived") or f.page.url.endswith("loadings-for-evaluator"), \
        f"Unexpected URL: {page.url}"
