#!/usr/bin/python3
"""
This module provides a function for adding two integers.

It defines a single function, add_integer(a, b=98),
which returns the sum of the two given numbers.
Both arguments must be integers or floats.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats.

    Returns the sum of a and b after converting
    float arguments to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a doit être un entier")
    if not isinstance(b, (int, float)):
        raise TypeError("b doit être un entier")
    return int(a) + int(b)
