import allure
import pytest
from extensions.functions import Functions


@pytest.mark.sanity
@allure.story("טסט 1")
@allure.description("תיאור טסט 1")
def test_normal_loading(initialize_pages, add_allure_attach):
   initialize_pages['Functions'].
   initialize_pages['WorkFlow'].
   initialize_pages['LoadingPage'].


