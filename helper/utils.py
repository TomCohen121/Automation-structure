import os

import yaml


def path_from_project_root(file_path: str) -> str:
    _root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return _root_dir + '/' + file_path

regular_loading_number_E2E = None
regular_loading_number_error_handling = None
regular_loading_number_E2E_half_discharge = None
regular_loading_number_E2E_set_suspicious_notebook = None
regular_loading_number_E2E_set_uncheck_notebook = None


def load_numbers_from_yaml(file_path):
    global regular_loading_number_E2E, regular_loading_number_error_handling, regular_loading_number_E2E_half_discharge
    global regular_loading_number_E2E_set_uncheck_notebook, regular_loading_number_E2E_set_suspicious_notebook

    with open(file_path, 'r') as yaml_file:  # טוען את קובץ ה-YAML
        config = yaml.safe_load(yaml_file)  # טוען את הנתונים מקובץ YAML

    # שליפת הערכים ממבנה ה-YAML
    regular_loading_number_E2E = config["loading_numbers"]["regular_loading_number_E2E"]
    regular_loading_number_error_handling = config["loading_numbers"]["regular_loading_number_error_handling"]
    regular_loading_number_E2E_half_discharge = config["loading_numbers"]["regular_loading_number_E2E_half_discharge"]
    regular_loading_number_E2E_set_suspicious_notebook = config["loading_numbers"]["regular_loading_number_E2E_set_suspicious_notebook"]
    regular_loading_number_E2E_set_uncheck_notebook = config["loading_numbers"]["regular_loading_number_E2E_set_uncheck_notebook"]

# שינוי הנתיב לקובץ YAML
yaml_file_path = 'C:/Automation/Projects/marvad_automation/resources/Configuration.yml'
load_numbers_from_yaml(yaml_file_path)  # קריאה לפונקציה עם קובץ YAML
