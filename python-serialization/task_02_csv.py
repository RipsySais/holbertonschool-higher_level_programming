#!/usr/bin/env python3
"""
Module pour convertir un fichier CSV en JSON
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en fichier JSON.

    Args:
        csv_filename (str): Le nom du fichier CSV source.

    Returns:
        bool: True si la conversion réussit, False sinon.
    """
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return True

    except (FileNotFoundError, IOError):
        return False
