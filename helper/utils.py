import os
import xml.etree.ElementTree as ET

def path_from_project_root(file_path: str) -> str:
    _root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return _root_dir + '/' + file_path


loading_number = None
def load_number_from_xml(file_path):
    global loading_number
    tree = ET.parse(file_path)
    root = tree.getroot()
    loading_number = root.find('number').text
xml_file_path = 'C:/Automation/Projects/marvad_automation/LoadingNumber.xml'
load_number_from_xml(xml_file_path)