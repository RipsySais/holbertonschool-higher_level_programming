#!/usr/bin/python3
"""
This module defines a class BaseGeometry
Ce module définit une classe appelée BaseGeometry
"""


class BaseGeometry:
    """
    A class BaseGeometry with a method area()
    Une classe BaseGeometry avec une méthode area()
    """

    def area(self):
        """
        Calculate the area of the geometry.
        Calcule l'aire de la géométrie.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value.
        Valide la valeur.
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
