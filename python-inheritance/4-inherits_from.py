#!/usr/bin/python3
"""Module that return true if
object is exactly an instance of the specified class
"""


def inherits_from(obj, a_class):
    """Function that return true if
    object is exactly an instance of the specified class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
