import sys
import json
from typing import TextIO

fileVariable: TextIO = open('C:/Users/samee/PycharmProjects/pythonProject/Webpage/result.txt', 'r+')
fileVariable.truncate(0)
fileVariable.close()

with open("mitre.json") as json_file:
    data = json.load(json_file)
    for c in data['result']:
        file_path = 'C:/Users/samee/PycharmProjects/pythonProject/webpage/result.txt'
        sys.stdout = open(file_path, "a")
        print('Output')
        print("ID: " + c["cve/CVE_data_meta/ID"])
        print("Description: " + c["cve/CVE_data_meta/ID"])
        print("Metadata assigner: " + c["cve/CVE_data_meta/ASSIGNER"])
        print("cvss vector string: " + c['impact/baseMetricV3/cvssV3/vectorString'])
        print("Published on: " + c["publishedDate"])
        print("Last Modified: " + c["lastModifiedDate"])

