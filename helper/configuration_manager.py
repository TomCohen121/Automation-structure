import os
import xml.etree.ElementTree as ET

from playwright.async_api import Playwright, BrowserType


class ConfigurationManager:
    _config = None

    @staticmethod
    def load_config():
        config_file_path = os.path.join(os.path.dirname(__file__), 'C:/Automation/Projects/marvad_automation/resources/Configuration.xml')
        tree = ET.parse(config_file_path)
        ConfigurationManager._config = ET.parse(config_file_path).getroot()  # ניתוח קובץ ה-XML
        return ConfigurationManager._config

    @staticmethod
    def get_browser():
        return ConfigurationManager._config.find('browser').text

    @staticmethod
    def is_headless():
        return ConfigurationManager._config.find('headless').text.lower() == 'true'

    @staticmethod
    def get_slow_motion():
        return int(ConfigurationManager._config.find('slow_motion').text)

    @staticmethod
    def base_url():
        return ConfigurationManager._config.find('base_url').text

    @staticmethod
    def maximize_window():
        return ConfigurationManager._config.find('maximize_window').text.lower() == 'true'


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
        context = browser.new_context(viewport={"width": 1920, "height": 1080} if ConfigurationManager.maximize_window() else {})
        page = context.new_page()
        return browser, page
