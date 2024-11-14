import os
import yaml


def path_from_project_root(file_path: str) -> str:
    _root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(_root_dir, file_path)  # השתמש ב-os.path.join להבטיח תאימות בין מערכות הפעלה

# Regular Loading
regular_loading_E2E_num = None
regular_loading_error_num = None
regular_loading_half_discharge_num = None
regular_loading_set_suspicious_num = None
regular_loading_set_unchecked_num = None

# After Appeal Loading
appeal_loading_E2E_num = None
appeal_loading_error_num = None
appeal_loading_half_discharge_num = None
appeal_loading_set_suspicious_num = None
appeal_loading_set_unchecked_num = None

# Suspicious Loading
suspicious_loading_approve_num = None
suspicious_loading_denied_num = None
suspicious_loading_error_num = None
suspicious_loading_half_discharge_num = None
suspicious_loading_set_unchecked_num = None

# MisMatch Loading
misMatch_loading_E2E_num = None
misMatch_loading_set_suspicious_num = None
misMatch_loading_error_num = None
misMatch_loading_half_discharge_num = None
misMatch_loading_set_unchecked_num = None

# Sample Loading
sample_loading_E2E_num = None
sample_loading_set_suspicious_num = None
sample_loading_error_num = None
sample_loading_half_discharge_num = None
sample_loading_set_unchecked_num = None

def load_numbers_from_yaml(file_path):
    global regular_loading_E2E_num, regular_loading_error_num, regular_loading_half_discharge_num
    global regular_loading_set_suspicious_num, regular_loading_set_unchecked_num
    global appeal_loading_E2E_num, appeal_loading_error_num, appeal_loading_half_discharge_num
    global appeal_loading_set_suspicious_num, appeal_loading_set_unchecked_num
    global suspicious_loading_approve_num, suspicious_loading_denied_num, suspicious_loading_error_num, suspicious_loading_half_discharge_num
    global suspicious_loading_set_unchecked_num
    global misMatch_loading_E2E_num, misMatch_loading_set_suspicious_num, misMatch_loading_error_num
    global misMatch_loading_half_discharge_num, misMatch_loading_set_unchecked_num
    global sample_loading_E2E_num, sample_loading_set_suspicious_num, sample_loading_error_num
    global sample_loading_half_discharge_num, sample_loading_set_unchecked_num


    with open(file_path, 'r') as yaml_file:  # טוען את קובץ ה-YAML
        config = yaml.safe_load(yaml_file)  # טוען את הנתונים מקובץ YAML

    regular_loading_E2E_num = config["loading_numbers"]["regular_loading_E2E_num"]
    regular_loading_error_num = config["loading_numbers"]["regular_loading_error_num"]
    regular_loading_half_discharge_num = config["loading_numbers"]["regular_loading_half_discharge_num"]
    regular_loading_set_suspicious_num = config["loading_numbers"]["regular_loading_set_suspicious_num"]
    regular_loading_set_unchecked_num = config["loading_numbers"]["regular_loading_set_unchecked_num"]

    appeal_loading_E2E_num = config["loading_numbers"]["appeal_loading_E2E_num"]
    appeal_loading_error_num = config["loading_numbers"]["appeal_loading_error_num"]
    appeal_loading_half_discharge_num = config["loading_numbers"]["appeal_loading_half_discharge_num"]
    appeal_loading_set_suspicious_num = config["loading_numbers"]["appeal_loading_set_suspicious_num"]
    appeal_loading_set_unchecked_num = config["loading_numbers"]["appeal_loading_set_unchecked_num"]

    suspicious_loading_approve_num = config["loading_numbers"]["suspicious_loading_approve_num"]
    suspicious_loading_denied_num = config["loading_numbers"]["suspicious_loading_denied_num"]
    suspicious_loading_error_num = config["loading_numbers"]["suspicious_loading_error_num"]
    suspicious_loading_half_discharge_num = config["loading_numbers"]["suspicious_loading_half_discharge_num"]
    suspicious_loading_set_unchecked_num = config["loading_numbers"]["suspicious_loading_set_unchecked_num"]

    misMatch_loading_E2E_num = config["loading_numbers"]["misMatch_loading_E2E_num"]
    misMatch_loading_set_suspicious_num = config["loading_numbers"]["misMatch_loading_set_suspicious_num"]
    misMatch_loading_error_num = config["loading_numbers"]["misMatch_loading_error_num"]
    misMatch_loading_half_discharge_num = config["loading_numbers"]["misMatch_loading_half_discharge_num"]
    misMatch_loading_set_unchecked_num = config["loading_numbers"]["misMatch_loading_set_unchecked_num"]

    sample_loading_E2E_num = config["loading_numbers"]["sample_loading_E2E_num"]
    sample_loading_set_suspicious_num = config["loading_numbers"]["sample_loading_set_suspicious_num"]
    sample_loading_error_num = config["loading_numbers"]["sample_loading_error_num"]
    sample_loading_half_discharge_num = config["loading_numbers"]["sample_loading_half_discharge_num"]
    sample_loading_set_unchecked_num = config["loading_numbers"]["sample_loading_set_unchecked_num"]

yaml_file_path = path_from_project_root('resources/Configuration.yml')
load_numbers_from_yaml(yaml_file_path)  # קריאה לפונקציה עם קובץ YAML
