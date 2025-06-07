#!/usr/bin/env python3
"""
Module pour sérialiser et désérialiser des objets
Python personnalisés avec pickle.
"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'objet courant dans un fichier avec pickle.
        Args:
            filename (str): Nom du fichier de destination.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass  # Tu peux aussi logger l'erreur si nécessaire

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet depuis un fichier pickle.
        Args:
            filename (str): Nom du fichier source.
        Returns:
            CustomObject ou None si erreur.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
