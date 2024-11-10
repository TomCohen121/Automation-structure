import os
import yaml


def path_from_project_root(file_path: str) -> str:
    _root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(_root_dir, file_path)  # השתמש ב-os.path.join להבטיח תאימות בין מערכות הפעלה

# Regular Loading
regular_loading_number_E2E = None
regular_loading_number_error_handling = None
regular_loading_number_E2E_half_discharge = None
regular_loading_number_E2E_set_suspicious_notebook = None
regular_loading_number_E2E_set_uncheck_notebook = None

# After Appeal Loading
after_appeal_loading_number_E2E = None
after_appeal_number_error_handling = None
after_appeal_number_E2E_half_discharge = None
after_appeal_number_E2E_set_suspicious_notebook = None
after_appeal_number_E2E_set_uncheck_notebook = None

# Suspicious Loading
suspicious_loading_number_E2E_approve = None
suspicious_loading_number_E2E_denied = None
suspicious_number_error_handling = None
suspicious_number_E2E_half_discharge = None
suspicious_number_E2E_set_uncheck_notebook = None

def load_numbers_from_yaml(file_path):
    global regular_loading_number_E2E, regular_loading_number_error_handling, regular_loading_number_E2E_half_discharge
    global regular_loading_number_E2E_set_uncheck_notebook, regular_loading_number_E2E_set_suspicious_notebook
    global after_appeal_loading_number_E2E, after_appeal_number_error_handling, after_appeal_number_E2E_half_discharge
    global after_appeal_number_E2E_set_suspicious_notebook, after_appeal_number_E2E_set_uncheck_notebook
    global suspicious_loading_number_E2E_approve, suspicious_loading_number_E2E_denied, suspicious_number_error_handling, suspicious_number_E2E_half_discharge
    global suspicious_number_E2E_set_uncheck_notebook

    with open(file_path, 'r') as yaml_file:  # טוען את קובץ ה-YAML
        config = yaml.safe_load(yaml_file)  # טוען את הנתונים מקובץ YAML

    # שליפת הערכים ממבנה ה-YAML
    regular_loading_number_E2E = config["loading_numbers"]["regular_loading_number_E2E"]
    regular_loading_number_error_handling = config["loading_numbers"]["regular_loading_number_error_handling"]
    regular_loading_number_E2E_half_discharge = config["loading_numbers"]["regular_loading_number_E2E_half_discharge"]
    regular_loading_number_E2E_set_suspicious_notebook = config["loading_numbers"]["regular_loading_number_E2E_set_suspicious_notebook"]
    regular_loading_number_E2E_set_uncheck_notebook = config["loading_numbers"]["regular_loading_number_E2E_set_uncheck_notebook"]

    after_appeal_loading_number_E2E = config["loading_numbers"]["after_appeal_loading_number_E2E"]
    after_appeal_number_error_handling = config["loading_numbers"]["after_appeal_number_error_handling"]
    after_appeal_number_E2E_half_discharge = config["loading_numbers"]["after_appeal_number_E2E_half_discharge"]
    after_appeal_number_E2E_set_suspicious_notebook = config["loading_numbers"]["after_appeal_number_E2E_set_suspicious_notebook"]
    after_appeal_number_E2E_set_uncheck_notebook = config["loading_numbers"]["after_appeal_number_E2E_set_uncheck_notebook"]

    suspicious_loading_number_E2E_approve = config["loading_numbers"]["suspicious_loading_number_E2E_approve"]
    suspicious_loading_number_E2E_denied = config["loading_numbers"]["suspicious_loading_number_E2E_denied"]
    suspicious_number_error_handling = config["loading_numbers"]["suspicious_number_error_handling"]
    suspicious_number_E2E_half_discharge = config["loading_numbers"]["suspicious_number_E2E_half_discharge"]
    suspicious_number_E2E_set_uncheck_notebook = config["loading_numbers"]["suspicious_number_E2E_set_uncheck_notebook"]


# שינוי הנתיב לקובץ YAML לנתיב יחסי
yaml_file_path = path_from_project_root('resources/Configuration.yml')
load_numbers_from_yaml(yaml_file_path)  # קריאה לפונקציה עם קובץ YAML
