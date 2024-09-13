#!/usr/bin/python3
"""defines a single function for json file inter-operability
"""

import json


def from_json_string(jstring):
    """returns a python object defined by the given json string representation
    """
    return json.loads(jstring)
