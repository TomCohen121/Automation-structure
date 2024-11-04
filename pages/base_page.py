from playwright.sync_api import Page
from helper.configuration_manager import ConfigurationManager

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.loadingPage = None
        self.check_notebookPage = None
        self.notebookPage = None
        self.personal_areaPage = None
        self.portionPage = None
        self.functions = None
        self.workflow = None
        self.breadcrumbs = None

    def goto(self, url=None):
        self.page.goto(url or ConfigurationManager.base_url())
        return self

    def initialize_all_pages(self):
        from pages.portions_page import PortionPage
        from pages.loading_page import LoadingPage
        from extensions.functions import Functions
        from flows.web_flows import WorkFlow
        from pages.check_notebook_page import CheckNotebookPage
        from pages.notebook_page import NotebookPage
        from pages.personal_area_page import PersonalAreaPage
        from pages.breadcrumbs import Breadcrumbs

        self.loadingPage = LoadingPage(self.page)
        self.check_notebookPage = CheckNotebookPage(self.page)
        self.notebookPage = NotebookPage(self.page)
        self.personal_areaPage = PersonalAreaPage(self.page)
        self.portionPage = PortionPage(self.page)
        self.functions = Functions(self.page)
        self.workflow = WorkFlow(self.page)
        self.breadcrumbs = Breadcrumbs(self.page)


    @staticmethod
    def goto_homepage(pages):
        pages.loadingPage.goto()

