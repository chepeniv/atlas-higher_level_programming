#!/usr/bin/python3
"""defines a single function for json file inter-operability
"""

import json


def to_json_string(obj):
    """returns the json representation of the given object
    """
    return json.dumps(obj)
