#!/usr/bin/env python3
"""
Module pour la sérialisation et désérialisation d'un dictionnaire en XML
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire Python dans un fichier XML.

    Args:
        dictionary (dict): Le dictionnaire à sérialiser.
        filename (str): Le nom du fichier XML de sortie.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python.

    Args:
        filename (str): Le fichier XML à lire.

    Returns:
        dict: Le dictionnaire reconstruit.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for element in root:
            result[element.tag] = element.text

        return result
    except (ET.ParseError, FileNotFoundError):
        return None
