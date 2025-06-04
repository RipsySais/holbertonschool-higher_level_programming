#!/usr/bin/python3
"""
This module provides a function `add_integer` to add two integers or floats.

The function has two parameters, `a` and `b`,
and returns their sum as an integer.
If either `a` or `b` is not an integer or float, a `TypeError` will be raised.

Examples:
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
    ...
TypeError: b must be an integer
"""


def add_integer(a, b=98):

    """
    Function that adds 2 integers.
    Args:
        a: integer
        b: integer
    Returns:
        The addition of the 2 integers
    Raises:
        TypeError: If a or b is not an integer or float
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
