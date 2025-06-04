#!/usr/bin/python3

"""Module for print_square method
print_square: prints a square with the character #.
prototype: def print_square(size)
raises:
TypeError: if size is not an int
ValueError: if size is less than 0
TypeError: if size is a float and is less than 0
TypeError: if size is a float and is not a whole number
TypeError: if size is not an int
must use the character # to print the square
all characters must be separated by a new line
size is the size length of the square
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: The size length of the square.

    Raises:
        TypeError: if size is not an int
        ValueError: if size is less than 0
        TypeError: if size is a float and is less than 0
        TypeError: if size is a float and is not a whole number
        TypeError: if size is not an int
        must use the character # to print the square
        all characters must be separated by a new line
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size % 1 != 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
