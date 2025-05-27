#!/usr/bin/python3
"""
This module defines an abstract class BaseGeometry.
Ce module définit une classe abstraite BaseGeometry.
"""


class BaseGeometry:
    """
    A class BaseGeometry with a method area() and integer validation.
    Une classe BaseGeometry avec une méthode area() et une validation d'entier.
    """

    def area(self):
        """
        Calculate the area of the geometry.
        Calcule l'aire de la géométrie.
        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value.
        Valide la valeur.

        Args:
            name (str): The name of the parameter.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} doit être un entier")
        if value <= 0:
            raise ValueError(f"{name} doit être supérieur à 0")
