import os
import shutil
import smtplib
import subprocess
import zipfile
import allure

class ReportingManager:
    @staticmethod
    def generate_allure_report(allure_results_path, allure_report_path):
        try:
            # יצירת דוח Allure
            subprocess.run(f"allure generate {allure_results_path} -o {allure_report_path} --clean", check=True,
                           shell=True)
            ReportingManager.open_allure_report(allure_report_path)
        except subprocess.CalledProcessError as e:
            print(f"Error generating Allure report: {e}")
            raise

    @staticmethod
    def open_allure_report(report_path):
        os.system(f"allure open {report_path}")

    @staticmethod
    def attach_screenshot(page, name):
        allure.attach(page.screenshot(), name=name, attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def clean_allure_results(allure_results_path):
        """מנקה את תיקיית allure-results לפני כל הרצה."""
        if os.path.exists(allure_results_path):
            shutil.rmtree(allure_results_path)
        os.makedirs(allure_results_path)

