import os
import xml.etree.ElementTree as ET

def path_from_project_root(file_path: str) -> str:
    _root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return _root_dir + '/' + file_path


regular_loading_number = None
suspicious_loading_number = None
senior_loading_number = None
noncompliance_loading_number = None
afterAppeal_loading_number = None
sampleAfterEvaluation_loading_number = None

def load_numbers_from_xml(file_path):
    global regular_loading_number, suspicious_loading_number, senior_loading_number
    global noncompliance_loading_number, afterAppeal_loading_number, sampleAfterEvaluation_loading_number
    tree = ET.parse(file_path)
    root = tree.getroot()

    regular_loading_number = root.find('regular_loading_number').text
    suspicious_loading_number = root.find('suspicious_loading_number').text
    senior_loading_number = root.find('senior_loading_number').text
    noncompliance_loading_number = root.find('noncompliance_loading_number').text
    afterAppeal_loading_number = root.find('afterAppeal_loading_number').text
    sampleAfterEvaluation_loading_number = root.find('sampleAfterEvaluation_loading_number').text

xml_file_path = 'C:/Automation/Projects/marvad_automation/resources/Configuration.xml'
load_numbers_from_xml(xml_file_path)
