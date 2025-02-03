#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
Ce module définit une classe appelée BaseGeometry.
"""


class BaseGeometry:
    """
    A claas BaseGeometry with a method area().
    Une classe BaseGeometry avec une méthode area().
    """

    def area(self):
        """
        Calculate the area of the geometry.
        Calcule l'aire de la géométrie.
        """
        raise Exception("area() is not implemented")
