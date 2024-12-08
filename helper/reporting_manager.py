import os
import shutil
import smtplib
import subprocess
import zipfile
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
    def zip_allure_report(report_path):
        zip_file_path = "allure-report.zip"

        # דחיסת תיקיית הדוח כקובץ ZIP
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(report_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    # הוספת כל קובץ בתיקיה ל-ZIP עם שמות קבצים יחסיים
                    zipf.write(file_path, os.path.relpath(file_path, report_path))
        return zip_file_path

    @staticmethod
    def send_report(report_path):
        current_time = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        sender_email = "hitzhak@cambium.co.il"
        sender_password = "holw qybq gyta bihh"
        receiver_email = "ctom@cambium.co.il"
        subject = "תוצאות הרצת בדיקות אוטומציה במרבד"
        body = f"ההרצה האחרונה של בדיקות האוטומציה הסתיימה ב-{current_time}. מצורף דוח המפרט את התוצאות של כל הבדיקות שבוצעו"

        # יצירת קובץ ה-ZIP של הדוח
        zip_file_path = ReportingManager.zip_allure_report(report_path)

        # שליחה במייל
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with open(zip_file_path, 'rb') as report_file:
            report = MIMEBase('application', 'octet-stream')
            report.set_payload(report_file.read())
            encoders.encode_base64(report)
            report.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(zip_file_path)}"')
            msg.attach(report)

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                print(f"Report sent successfully to {receiver_email}.")
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")
            return

    @staticmethod
    def attach_screenshot(page, name):
        allure.attach(page.screenshot(), name=name, attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def clean_allure_results(allure_results_path):
        """מנקה את תיקיית allure-results לפני כל הרצה."""
        if os.path.exists(allure_results_path):
            shutil.rmtree(allure_results_path)
        os.makedirs(allure_results_path)

    # @staticmethod
    # def send_report_after_tests(report_path):
    #     ReportingManager.send_report(report_path)