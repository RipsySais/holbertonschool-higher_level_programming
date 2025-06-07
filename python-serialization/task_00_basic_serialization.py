#!/usr/bin/python3
"""
Sérialization and deserialization of Python objects
"""


import json


def seralize_and_save_to_file(data, filename):
    """
    Serialize data to a JSON file.
    Args:
        data (dict): The data to serialize.
        filename (str): The name of the file to save the serialized data.
    """
    with open(filename, 'w', encoding='UTF-8') as f:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_and_deserialize_from_file(filename):
    """
    Load and deserialize data from a JSON file.
    Args:
        filename (str): The name of the file to load the serialized data from.
    Returns:
        dict: The deserialized data.
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        return json.load(f)
