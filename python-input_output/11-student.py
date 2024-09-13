#!/usr/bin/python3
"""defines a single class with a json storage method
"""


class Student:
    """a custom student class
    """
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def to_json(self, attrs=None):
        json_dict = {}
        if attrs is None:
            json_dict.update({"first_name": self.first_name})
            json_dict.update({"last_name": self.last_name})
            json_dict.update({"age": self.age})
        else:
            for key in attrs:
                value = self.__dict__.get(key)
                if value is not None:
                    json_dict.update({key: value})
        return json_dict

    def reload_from_json(self, json_dict):
        for key in json_dict.keys():
            new_val = json_dict.get(key)
            old_val = self.__dict__.get(key)
            if old_val is not None:
                self.__dict__.update({key: new_val})
