#!/usr/bin/python3
"""
Module to convert an object to a JSON serializable dictionary.
"""


def class_to_json(obj):
    """
    Convert an object to a JSON serializable dictionary.

    Args:
        obj: The object to convert.

    Returns:
        A dictionary representation of the object.
    """
    return obj.__dict__
