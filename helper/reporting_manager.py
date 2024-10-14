import os
import smtplib
import subprocess
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import allure


class ReportingManager:
    @staticmethod
    def generate_allure_report(allure_results_path, allure_report_path):
        try:
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
    def send_report(report_path):
        current_time = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        sender_email = "hitzhak@cambium.co.il"
        sender_password = "holw qybq gyta bihh"
        receiver_email = "hitzhak@cambium.co.il"
        subject = "תוצאות הרצת בדיקות אוטומציה במרבד"
        body = f"ההרצה האחרונה של בדיקות האוטומציה הסתיימה ב-{current_time}. מצורף דוח המפרט את התוצאות של כל הבדיקות שבוצעו"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with open(report_path, 'rb') as report_file:
            report = MIMEBase('application', 'octet-stream')
            report.set_payload(report_file.read())
            encoders.encode_base64(report)
            report.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(report_path)}"')
            msg.attach(report)

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

    @staticmethod
    def attach_screenshot(page, name):
        allure.attach(page.screenshot(), name=name, attachment_type=allure.attachment_type.PNG)
    #
    # @staticmethod
    # def send_report_after_tests(report_path):
    #     ReportingManager.send_report(report_path)
