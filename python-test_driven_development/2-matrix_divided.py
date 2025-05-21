#!/usr/bin/python3
"""
Module contenant la fonction matrix_divided.
"""


def matrix_divided(matrice, div):
    """
    Divise tous les éléments d'une matrice par div.

    Args:
        matrice (list of lists): matrice d'entiers ou flottants.
        div (int or float): diviseur.

    Returns:
        list of lists: nouvelle matrice divisée arrondie à 2 décimales.

    Raises:
        TypeError: si matrice n'est pas une liste de listes d'int/float,
                   ou si les lignes n'ont pas la même taille,
                   ou si div n'est pas un nombre.
        ZeroDivisionError: si div est zéro.
    """
    if not isinstance(matrice, list) or \
       not all(isinstance(row, list) for row in matrice):
        raise TypeError(
            "La matrice doit être une matrice (liste de listes) "
            "d’entiers ou de flottants"
        )

    if len(matrice) == 0 or \
            any(len(row) != len(matrice[0]) for row in matrice):
        raise TypeError("Chaque ligne de la matrice doit avoir la même taille")

    for row in matrice:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "La matrice doit être une matrice (liste de listes) "
                    "d’entiers ou de flottants"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("La variable div doit être un nombre")
    if div == 0:
        raise ZeroDivisionError("Division par zéro")

    return [[round(elem / div, 2) for elem in row] for row in matrice]
