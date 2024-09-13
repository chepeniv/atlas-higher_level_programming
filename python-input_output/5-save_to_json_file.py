#!/usr/bin/python3
"""defines a single function for json file inter-operability
"""

import json


def save_to_json_file(obj, filename):
    """writes the json representation of given object into the given file
    """
    with open(filename, mode="w") as file:
        file.write(json.dumps(obj))
