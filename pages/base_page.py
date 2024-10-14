from playwright.sync_api import Playwright, Page

from extensions.functions import Functions
from flows.web_flows import WorkFlow
from helper.configuration_manager import ConfigurationManager

from extensions.functions import Functions
from pages.check_notebook_page import CheckNotebookPage
from pages.loading_page import LoadingPage
from pages.notebook_page import NotebookPage
from pages.personal_area_page import PersonalAreaPage
from pages.portions_page import PortionPage
from flows.web_flows import WorkFlow
from tests.conftest import initialize_pages


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url=None):
        self.page.goto(url or ConfigurationManager.base_url())
        return self

    @staticmethod
    def initialize_all_pages(page):
        loadingPage= LoadingPage(page)
        checkNotebook = CheckNotebookPage(page)
        noteBookPage = NotebookPage(page)
        personalAreaPage = PersonalAreaPage(page)
        functions = Functions(page)
        portionPage = PortionPage(page)
        workflow = WorkFlow(page)

        returnObject = {
            "CheckNotebookPage": checkNotebook,
            "LoadingPage": loadingPage,
            "NotebookPage": noteBookPage,
            "PersonalAreaPage": personalAreaPage,
            "PortionPage": portionPage,
            "Functions": functions,
            "WorkFlow": workflow,
        }

        return returnObject

    @staticmethod
    def goto_homepage(pages):
        pages['LoadingPage'].goto()


