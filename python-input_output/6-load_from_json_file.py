#!/usr/bin/python3
"""defines a single function for json file inter-operability
"""

import json


def load_from_json_file(filename):
    """reads data from json file and extracts python object
    """
    with open(filename) as file:
        line = file.read()
        return json.loads(line)
