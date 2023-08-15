import json
import os 
from os.path import dirname
import pathlib
from Tool import *
import ast


folder_path = dirname(dirname(pathlib.Path(__file__).parent.resolve()))
SWC_no = '117'
file_name = 'output'

tool = Tool(folder_path, SWC_no, file_name)

file_path = tool.join_path()
print(file_path)
with open(file_path, 'r') as output_json:
    data =  output_json.read()
data_dict = json.loads(data)

def find_contract (element):
    if element.get("type") == "pragma":
        return None
    else:
        if element.get("type") == "contract":
            return element.get("name")
        else:
            contract = find_contract(element["type_specific_fields"]["parent"])
            return contract 


def get_smallest_element(elements: list[dict]) -> dict:
    if (len(elements) == 0): 
        return {}
    elif (len(elements) == 1):
        return elements[0]
    else:
        for element in elements:
            #TODO:will add more
            if element["type"] == "node":
                return element
            
    return elements[0]

def list_elements (detectors: list[Ana]):
    for detector in detectors:
        elements = detector.get("elements")
        element = get_smallest_element(elements)
        element_name = element.get("name")
            contract = find_contract(element)
            description = detector.get("description", "")
            lines = element.get("source_mapping", {}).get("lines", [])
            check = detector.get("check", "")
            print("Element Name:", element_name)
            print("Contract Name:", contract)
            print("Description:", description)
            print("Lines:", lines)
            print("Check:", check)
            print("----------")

            
# print (type(data_dict["results"]["detectors"]))
print(list_elements(data_dict["results"]["detectors"]) ) 
