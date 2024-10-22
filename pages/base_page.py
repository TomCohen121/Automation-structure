from playwright.sync_api import Page
from helper.configuration_manager import ConfigurationManager


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url=None):
        self.page.goto(url or ConfigurationManager.base_url())
        return self

    @staticmethod
    def initialize_all_pages(page):
        from pages.portions_page import PortionPage
        from pages.loading_page import LoadingPage
        from extensions.functions import Functions
        from flows.web_flows import WorkFlow
        from pages.check_notebook_page import CheckNotebookPage
        from pages.notebook_page import NotebookPage
        from pages.personal_area_page import PersonalAreaPage
        from pages.breadcrumbs import Breadcrumbs

        pages = {}
        pages["LoadingPage"] = LoadingPage(page)
        pages["CheckNotebookPage"] = CheckNotebookPage(page)
        pages["NotebookPage"] = NotebookPage(page)
        pages["PersonalAreaPage"] = PersonalAreaPage(page)
        pages["PortionPage"] = PortionPage(page)
        pages["Functions"] = Functions(page)
        pages["WorkFlow"] = WorkFlow(page)
        pages["Breadcrumbs"] = Breadcrumbs(page)
        return pages

    @staticmethod
    def goto_homepage(pages):
        pages['LoadingPage'].goto()


