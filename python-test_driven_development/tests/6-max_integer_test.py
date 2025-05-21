#!/usr/bin/python3
"""Unittest pour max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Classe de test pour la fonction max_integer()"""

    def test_list_positive_numbers(self):
        """Test avec une liste de nombres positifs"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_list_negative_numbers(self):
        """Test avec une liste de nombres négatifs"""
        self.assertEqual(max_integer([-1, -5, -3, -10]), -1)

    def test_list_mixed_numbers(self):
        """Test avec une liste de nombres positifs et négatifs"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_list_one_element(self):
        """Test avec une liste contenant un seul élément"""
        self.assertEqual(max_integer([7]), 7)

    def test_list_empty(self):
        """Test avec une liste vide"""
        self.assertIsNone(max_integer([]))

    def test_list_identical_elements(self):
        """Test avec une liste contenant des éléments identiques"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_list_unordered(self):
        """Test avec une liste non triée"""
        self.assertEqual(max_integer([3, 7, 1, 9, 4]), 9)

    def test_not_a_list(self):
        """Test avec un type invalide"""
        with self.assertRaises(TypeError):
            max_integer("not a list")
        with self.assertRaises(TypeError):
            max_integer(42)
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
