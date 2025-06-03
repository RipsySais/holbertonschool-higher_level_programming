#!/usr/bin/python3
"""
Renvoie un abject à partir d'une chaîne JSON.

    Args:
        my_str (str): La chaîne JSON à convertir en objet.

    Returns:
        object: L'objet Python correspondant à la chaîne JSON.
"""


import json


def from_json_string(my_str):
    """Renvoie un abject à partir d'une chaîne JSON.

    Args:
        my_str (str): La chaîne JSON à convertir en objet.

    Returns:
        object: L'objet Python correspondant à la chaîne JSON.
    """
    return json.loads(my_str)
