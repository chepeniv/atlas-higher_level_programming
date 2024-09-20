#!/usr/bin/python3
""" barebones module holding a single class
"""


import json


class Base:
    """ a simple class that currently only handles id assignments
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializer for Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(dict_list):
        """ a function that builds a json string representation of
        a list of dictinaries
        """
        json_string = ""
        if dict_list is None or len(dict_list) == 0:
            return "[]"
        else:
            json_string += "["
            for dictionary in dict_list:
                json_string += json.dumps(dictionary)
                json_string += ", "
            json_string += "]"
            return json_string
