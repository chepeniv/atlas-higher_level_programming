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
        if dict_list is None or len(dict_list) == 0:
            return "[]"
        else:
            return json.dumps(dict_list)
            """
            json_string += "["
            for index in range(len(dict_list) - 1):
                json_string += json.dumps(dict_list[index])
                json_string += ", "
            json_string += json.dumps(dict_list[-1])
            json_string += "]"
            """
