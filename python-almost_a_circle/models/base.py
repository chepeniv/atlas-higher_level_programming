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

    @classmethod
    def save_to_file(cls, list_of_objects):
        """ takes a json string and saves it to a file
        """
        if list_of_objects is None:
            list_of_objects = []

        list_of_dicts = []
        for index in range(len(list_of_objects)):
            list_of_dicts.append(list_of_objects[index].to_dictionary())
            """ it is really interesting that i can call a method only
            defined in the child class from within its parent class
            """

        json_string = cls.to_json_string(list_of_dicts)

        # type() wasn't returning the correct type
        if str(cls).find("Rectangle") > 0:
            filename = "Rectangle"
        elif str(cls).find("Square") > 0:
            filename = "Square"
        else:
            filename = "Base"

        with open(filename + ".json", "w") as jsonfile:
            jsonfile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ takes a json string and returns a list object
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **desc):
        """
        """
        if str(cls).find("Rectangle") > 0:
            instance = cls(1, 1)
            instance.update(
                    width=desc.get('width'),
                    height=desc.get('height'),
                    )
        elif str(cls).find("Square") > 0:
            instance = cls(1)
            instance.update(size=desc.get('size'))

        instance.update(
                x=desc.get('x'),
                y=desc.get('y'),
                id=desc.get('id')
                )

        return instance
