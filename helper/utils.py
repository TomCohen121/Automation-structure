import os
import yaml

def path_from_project_root(file_path: str) -> str:
    _root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(_root_dir, file_path)  # השתמש ב-os.path.join להבטיח תאימות בין מערכות הפעלה

# Regular Loading
regular_loading_num = None
regular_loading_for_discharge = None
answer_law = None

# After Appeal Loading
appeal_loading_num = None
appeal_loading_for_discharge = None

# Suspicious Loading
suspicious_loading_num = None
suspicious_loading_for_discharge = None

# MisMatch Loading
misMatch_loading_num = None
misMatch_loading_for_discharge = None

# Senior Loading
senior_loading_num = None
senior_loading_for_discharge = None


def load_numbers_from_yaml(file_path):
    global regular_loading_num, regular_loading_for_discharge, answer_law
    global appeal_loading_num, appeal_loading_for_discharge
    global suspicious_loading_num, suspicious_loading_for_discharge
    global misMatch_loading_num, misMatch_loading_for_discharge
    global senior_loading_num, senior_loading_for_discharge

    with open(file_path, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)

    loading_numbers = config.get("loading_numbers", {})

    # Regular Loading
    regular_loading_num = loading_numbers.get("regular_loading_num")
    regular_loading_for_discharge = loading_numbers.get("regular_loading_num_for_discharge")
    answer_law = loading_numbers.get("answer_law")

    # After Appeal Loading
    appeal_loading_num = loading_numbers.get("appeal_loading_num")
    appeal_loading_for_discharge = loading_numbers.get("appeal_loading_for_discharge")

    # Suspicious Loading
    suspicious_loading_num = loading_numbers.get("suspicious_loading_num")
    suspicious_loading_for_discharge = loading_numbers.get("suspicious_loading_for_discharge")

    # MisMatch Loading
    misMatch_loading_num = loading_numbers.get("misMatch_loading_num")
    misMatch_loading_for_discharge = loading_numbers.get("misMatch_loading_for_discharge")

    # Senior Loading
    senior_loading_num = loading_numbers.get("senior_loading_num")
    senior_loading_for_discharge = loading_numbers.get("senior_loading_for_discharge")


yaml_file_path = path_from_project_root('resources/Configuration.yml')
load_numbers_from_yaml(yaml_file_path)  # קריאה לפונקציה עם קובץ YAML
