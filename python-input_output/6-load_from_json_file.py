#!/usr/bin/python3
"""
Charge un objet a parir d'un fichier JSON.
"""
import json


def load_from_json_file(filename):

    """
    Charge un objet à partir d'un fichier JSON.

    Args:
        filename (str): Nom du fichier à partir duquel charger l'objet JSON.

    Returns:
        object: L'objet chargé depuis le fichier JSON.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
