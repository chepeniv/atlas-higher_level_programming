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

    def to_json(self):
        json_dict = {}
        json_dict.update({"first_name": self.first_name})
        json_dict.update({"last_name": self.last_name})
        json_dict.update({"age": self.age})
        return json_dict
