#!/usr/bin/python3
"""defines a single function for json file inter-operability
"""


def class_to_json(obj):
    jdict = {}
    pydict = obj.__dict__
    for key in pydict.keys():
        if key[0] != '_':
            jdict.update({key: pydict.get(key)})

    return jdict


