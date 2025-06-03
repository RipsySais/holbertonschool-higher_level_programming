#!/usr/bin/python3
"""Écrit un objet dans un fichier texte en utilisant une représentation JSON.

    Args:
        my_obj (object): L'objet à enregistrer en JSON.
        filename (str): Nom du fichier dans lequel écrire l'objet JSON.
    """


import json


def save_to_json_file(my_obj, filename):
    """Écrit un objet dans un fichier texte en utilisant
     une représentation JSON.

    Args:
        my_obj (object): L'objet à enregistrer en JSON.
        filename (str): Nom du fichier dans lequel écrire l'objet JSON.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
