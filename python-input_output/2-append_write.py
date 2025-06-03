#!/usr/bin/python3
"""
Ajoute une chaîne à la fin d'un fichier texte UTF-8 et retourne le nombre
de caractères ajoutés.
"""


def append_write(filename="", text=""):
    """
Ajoute une chaîne à la fin d'un fichier texte UTF-8 et retourne le nombre
de caractères ajoutés.


    Args:
        filename (str): Le nom du fichier.
        text (str): Le texte à ajouter.

    Returns:
        int: Le nombre de caractères ajoutés.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
