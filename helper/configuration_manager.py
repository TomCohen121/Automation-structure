import os
import shutil
import subprocess
import sys
import pytest
import yaml
from playwright.sync_api import Playwright, BrowserType
from pytest_playwright.pytest_playwright import playwright
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class ConfigurationManager:
    _config = None
    _permissions = None
    _token = None

    @staticmethod
    def main():
        ConfigurationManager.cleanup_allure_results()  # הוספת קריאה לפונקציה למחיקת התיקייה
        ConfigurationManager.run_tests()

    @staticmethod
    def load_config():
        # נתיב יחסי לקובץ ה-YAML
        config_file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'Configuration.yml')
        with open(config_file_path, 'r') as config_file:
            ConfigurationManager._config = yaml.safe_load(config_file)  # טוען את קובץ ה-YAML
        return ConfigurationManager._config

    @staticmethod
    def cleanup_allure_results():
        allure_results_dir = os.path.join(os.path.dirname(__file__), '..', 'allure-results')
        # מחיקת תיקיית allure-results אם קיימת
        if os.path.exists(allure_results_dir):
            shutil.rmtree(allure_results_dir)
            print("Deleted allure-results folder")

    @staticmethod
    def load_permissions():
        if ConfigurationManager._permissions is None:
            permissions_file_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'permissions.yml')  # שם הקובץ שונה
            with open(permissions_file_path, 'r') as permissions_file:
                ConfigurationManager._permissions = yaml.safe_load(permissions_file)  # טוען את הקובץ החדש
        return ConfigurationManager._permissions

    @staticmethod
    def get_permission():
        config = ConfigurationManager.load_config()
        return config.get("permissions", "Regular Evaluator")  # ברירת מחדל: Regular

    @staticmethod
    def get_tags_for_permission(permission):
        roles_tags = ConfigurationManager.load_permissions()
        return roles_tags.get(permission, [])  # מחזיר רשימה ריקה אם אין תגיות

    @staticmethod
    def run_tests():
        # מקבל את ההרשאה
        permission = ConfigurationManager.get_permission()
        # טוען את התגיות לפי ההרשאה
        tags = ConfigurationManager.get_tags_for_permission(permission)
        if not tags:
            print(f"No tags found for permission: {permission}")
            return
        print(f"Running tests for permission: {permission} with tags: {tags}")
        tag_expression = " or ".join(tags)  # מחבר את כל התגיות עם OR
        pytest.main([
            "-m", tag_expression,  # מריץ את הבדיקות עם התגיות
            "--alluredir=allure-results",  # שמירת תוצאות Allure בתיקייה allure-results
            # "-n", "auto", # מפעיל את התהליכים במקביל
            "-r", "a",
        ])
        subprocess.run([r"C:\Automation\allure-2.30.0\bin\allure.bat", "serve", "allure-results"])

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
        selected_url = ConfigurationManager._config["environment"]
        url_map = {
            "QA": "https://djmgx4dl196h1.cloudfront.net/?f5=",
            "DEV": "https://d1dltc9sqvdor1.cloudfront.net/?f5="
        }
        base_url = url_map.get(selected_url)
        selected_token = ConfigurationManager._config["user_token"]
        token_map = {
            "Regular Evaluator": "ZjVTU089ZjVTU091c2VyPTAyNDkwMDczMCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
            "Senior Evaluator": "ZjVTU089ZjVTU091c2VyPTMwMjI4ODk5OCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Njc4",
            "Development Worker": "ZjVTU089ZjVTU091c2VyPTIwNTQ1MzQ1OSZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
            "Assessment Section Manager": "ZjVTU089ZjVTU091c2VyPTMxNjQ3NTgxMyZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ngo=",
            "Marvad CEO": "ZjVTU089ZjVTU091c2VyPTMyOTMxMzcwNCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
            "System Administrator": "ZjVTU089ZjVTU091c2VyPTMzOTQzMjIzOSZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
            "Mafmar": "ZjVTU089ZjVTU091c2VyPTAzNzMxMDM2NCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
            "Professional Manager": "ZjVTU089ZjVTU091c2VyPTMxMjY2ODMyMCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
        }
        token = token_map.get(selected_token)
        if base_url and token:
            return f"{base_url}{token}"  # מחבר את ה-URL וה-token
        return None

    @staticmethod
    def token_url():
        selected_token = ConfigurationManager._config["user_token"]
        token_map = {
            "Regular Evaluator": "ZjVTU089ZjVTU091c2VyPTAyNDkwMDczMCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
            "Senior Evaluator": "ZjVTU089ZjVTU091c2VyPTMwMjI4ODk5OCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Njc4",
            "Development Worker": "ZjVTU089ZjVTU091c2VyPTIwNTQ1MzQ1OSZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
            "Assessment Section Manager": "ZjVTU089ZjVTU091c2VyPTMxNjQ3NTgxMyZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ngo=",
            "Marvad CEO": "ZjVTU089ZjVTU091c2VyPTMyOTMxMzcwNCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
            "System Administrator": "ZjVTU089ZjVTU091c2VyPTMzOTQzMjIzOSZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
            "Mafmar": "ZjVTU089ZjVTU091c2VyPTAzNzMxMDM2NCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
            "Professional Manager": "ZjVTU089ZjVTU091c2VyPTMxMjY2ODMyMCZmNVNTT3Bhc3N3b3JkPTEyMzQ1Ng==",
        }
        return token_map.get(selected_token)

    @staticmethod
    def server_url(self):
        selected_environment = ConfigurationManager._config["environment"]
        if selected_environment == "DEV":
            selected_server_url = ConfigurationManager._config["server_url_DEV"]
        else:
            selected_server_url = ConfigurationManager._config["server_url_QA"]

        return selected_server_url

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
            "slow_mo": ConfigurationManager.get_slow_motion(),
            "args": ["--start-maximized"]  # פותח את הדפדפן במצב מסך מלא
        }
        browser = getattr(playwright, browser_type).launch(**browser_options)
        context = browser.new_context(no_viewport=True)
        page = context.new_page()
        page.evaluate("window.moveTo(0, 0); window.resizeTo(screen.width, screen.height);")
        return browser, page


if __name__ == "__main__":
    print("Starting ConfigurationManager...")
    ConfigurationManager.main()
