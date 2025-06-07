#!/usr/bin/python3
"""
Sérialisation et désérialisation d'objets Python.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise les données dans un fichier JSON.
    Args:
        data (dict): Les données à sérialiser.
        filename (str): Le nom du fichier JSON.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Charge et désérialise un fichier JSON.
    Args:
        filename (str): Le nom du fichier JSON à charger.
    Returns:
        dict: Les données désérialisées.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
