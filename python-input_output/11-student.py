#!/usr/bin/python3
""" Student module """


class Student:
    """ Defines a student with first name, last name, and age """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for key in attrs:
            if key in self.__dict__:
                new_dict[key] = self.__dict__[key]
        return new_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
