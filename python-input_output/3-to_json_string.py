#!/usr/bin/python3
"""Renvoie la représentation JSON d'un objet (chaîne).

    Args:
        my_obj: L'objet à convertir en JSON.

    Returns:
        str: La représentation JSON de l'objet.
    """


import json


def to_json_string(my_obj):
    """Renvoie la représentation JSON d'un objet (chaîne).

    Args:
        my_obj: L'objet à convertir en JSON.

    Returns:
        str: La représentation JSON de l'objet.
    """
    return json.dumps(my_obj)
