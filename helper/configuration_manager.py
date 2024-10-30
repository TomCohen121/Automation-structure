import os
import json
from playwright.sync_api import Playwright, BrowserType


class ConfigurationManager:
    _config = None

    @staticmethod
    def load_config():
        # נתיב לקובץ ה-JSON
        config_file_path = os.path.join(os.path.dirname(__file__), 'C:/Automation/Projects/marvad_automation/resources/Configuration.json')
        with open(config_file_path, 'r') as config_file:
            ConfigurationManager._config = json.load(config_file)  # טוען את קובץ ה-JSON
        return ConfigurationManager._config

    @staticmethod
    def get_browser():
        return ConfigurationManager._config["browser"]

    @staticmethod
    def is_headless():
        return ConfigurationManager._config["headless"]

    @staticmethod
    def get_slow_motion():
        return ConfigurationManager._config["slow_motion"]

    @staticmethod
    def base_url():
        return ConfigurationManager._config["base_url"]

    @staticmethod
    def maximize_window():
        return ConfigurationManager._config["maximize_window"]

    @staticmethod
    def get_loading_number(type_name):
        # מחזיר loading_number לפי סוג
        return ConfigurationManager._config["loading_numbers"].get(type_name)


class BrowserManager:
    @staticmethod
    def __get_browser_type(playwright: Playwright) -> BrowserType:
        browser = ConfigurationManager.get_browser()

        if browser == 'chromium':
            return playwright.chromium
        if browser == 'firefox':
            return playwright.firefox
        if browser == 'webkit':
            return playwright.webkit

    @staticmethod
    def setup(playwright: Playwright):
        ConfigurationManager.load_config()
        browser_type = ConfigurationManager.get_browser()
        browser_options = {
            "headless": ConfigurationManager.is_headless(),
            "slow_mo": ConfigurationManager.get_slow_motion()
        }
        browser = getattr(playwright, browser_type).launch(**browser_options)
        context = browser.new_context(viewport=None if ConfigurationManager.maximize_window() else {"width": 1920, "height": 1080})
        page = context.new_page()
        return browser, page
