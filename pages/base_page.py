from playwright.sync_api import Page
from helper.configuration_manager import ConfigurationManager

class BasePage:
    def __init__(self, page: Page):
        # When adding a new page, define its variable as None here
        self.page = page
        self.loadingPage = None
        self.checkNotebookPage = None
        self.notebookPage = None
        self.personalAreaPage = None
        self.portionPage = None
        self.functions = None
        self.workflow = None
        self.breadcrumbs = None
        self.suspiciousLoadingPortionPage = None
        self.suspiciousLoadingNotebookPage = None
        self.permissions = None
        self.messages = None
        self.personalDetailsPage = None

    def goto(self, url=None):
        self.page.goto(url or ConfigurationManager.base_url())
        return self

    def initialize_all_pages(self):
        #1. Import the new page class inside this function.
        #2. Assign the new page instance to the corresponding variable.
        from pages.portion_page import PortionPage
        from pages.loading_page import LoadingPage
        from extensions.functions import Functions
        from flows.workflows import WorkFlow
        from pages.check_notebook_page import CheckNotebookPage
        from pages.notebook_page import NotebookPage
        from pages.personal_area_page import PersonalAreaPage
        from pages.breadcrumbs import Breadcrumbs
        from pages.suspicious_loading_portions_page import SuspiciousLoadingPortionPage
        from pages.suspicious_loading_notebook_page import SuspiciousLoadingNotebookPage
        from pages.permissions import Permissions
        from pages.messages import Messages
        from pages.personal_details_page import PersonalDetailsPage

        self.loadingPage = LoadingPage(self.page)
        self.checkNotebookPage = CheckNotebookPage(self.page)
        self.notebookPage = NotebookPage(self.page)
        self.personalAreaPage = PersonalAreaPage(self.page)
        self.portionPage = PortionPage(self.page)
        self.functions = Functions(self.page)
        self.workflow = WorkFlow(self.page)
        self.breadcrumbs = Breadcrumbs(self.page)
        self.suspiciousLoadingPortionPage = SuspiciousLoadingPortionPage(self.page)
        self.suspiciousLoadingNotebookPage = SuspiciousLoadingNotebookPage(self.page)
        self.permissions = Permissions(self.page)
        self.messages = Messages(self.page)
        self.personalDetailsPage = PersonalDetailsPage(self.page)

    @staticmethod
    def goto_homepage(pages):
        pages.loadingPage.goto()

