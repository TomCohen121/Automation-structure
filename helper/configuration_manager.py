import os
import configparser
from playwright.sync_api import Playwright, BrowserType, Browser, Page


class ConfigurationManager:
    _config = configparser.ConfigParser()

    @staticmethod
    def load_config():
        config_file_path = os.path.join(os.path.dirname(__file__), 'C:/Automation/Projects/marvad_automation/resources/config.properties')
        ConfigurationManager._config.read(config_file_path)
        return ConfigurationManager._config['DEFAULT']

    @staticmethod
    def get_browser():
        return ConfigurationManager._config.get('DEFAULT', 'browser')

    @staticmethod
    def is_headless():
        return ConfigurationManager._config.getboolean('DEFAULT', 'headless')

    @staticmethod
    def get_slow_motion():
        return ConfigurationManager._config.getint('DEFAULT', 'slow.motion')

    @staticmethod
    def base_url():
        return ConfigurationManager._config.get('DEFAULT', 'base.url')

    @staticmethod
    def maximize_window():
        return ConfigurationManager._config.getboolean('DEFAULT', 'maximize.window', fallback=True)

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
        config = ConfigurationManager.load_config()
        browser_type = config.get('browser', 'chromium')
        browser_options = {
            "headless": config.getboolean('headless', False),
            "slow_mo": config.getint('slow.motion', 0)
        }
        browser = getattr(playwright, browser_type).launch(**browser_options)
        context = browser.new_context(viewport={"width": 1920, "height": 1080} if ConfigurationManager.maximize_window() else {})
        page = context.new_page()
        return browser, page
