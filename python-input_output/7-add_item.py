#!/usr/bin/python3
"""defines a single function for json file inter-operability
"""

import sys
import json


load_json = __import__('6-load_from_json_file').load_from_json_file
save_json = __import__('5-save_to_json_file').save_to_json_file

try:
    jdata = load_json('add_item.json')
except FileNotFoundError:
    jdata = []


for item in range(1, len(sys.argv)):
    jdata += [sys.argv[item]]

save_json(jdata, 'add_item.json')
