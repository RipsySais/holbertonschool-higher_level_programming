#!/usr/bin/python3
def print_square(size):
    """
    Affiche un carré avec le caractère #

    Arguments:
    size -- longueur du carré (doit être un entier >= 0)

    Exceptions:
    TypeError -- si size n'est pas un entier
    ValueError -- si size est < 0
    """

    if not isinstance(size, int):
        raise TypeError("la taille doit être un entier")
    if size < 0:
        raise ValueError("la taille doit être >= 0")

    for _ in range(size):
        print("#" * size)
