import os
import json


def path_from_project_root(file_path: str) -> str:
    _root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return _root_dir + '/' + file_path


regular_loading_number = None
suspicious_loading_number = None
senior_loading_number = None
noncompliance_loading_number = None
afterAppeal_loading_number = None
sampleAfterEvaluation_loading_number = None


def load_numbers_from_json(file_path):
    global regular_loading_number, suspicious_loading_number, senior_loading_number
    global noncompliance_loading_number, afterAppeal_loading_number, sampleAfterEvaluation_loading_number

    with open(file_path, 'r') as json_file:  # טוען את קובץ ה-JSON
        config = json.load(json_file)  # טוען את הנתונים לקובץ JSON

    # שליפת הערכים ממבנה ה-JSON
    regular_loading_number = config["loading_numbers"]["regular_loading_number"]
    suspicious_loading_number = config["loading_numbers"]["suspicious_loading_number"]
    senior_loading_number = config["loading_numbers"]["senior_loading_number"]
    noncompliance_loading_number = config["loading_numbers"]["noncompliance_loading_number"]
    afterAppeal_loading_number = config["loading_numbers"]["afterAppeal_loading_number"]
    sampleAfterEvaluation_loading_number = config["loading_numbers"]["sampleAfterEvaluation_loading_number"]


# שים לב לשנות את הנתיב לקובץ JSON
json_file_path = 'C:/Automation/Projects/marvad_automation/resources/Configuration.json'
load_numbers_from_json(json_file_path)  # קריאה לפונקציה עם קובץ JSON
