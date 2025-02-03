#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Vérifie si un objet est une instance d'une classe héritée d'une classe
Args:
obj (object): L'objet à vérifier
a_class (class): La classe à vérifier
Retourne:
bool: True si obj est une instance d'une classe héritée d'a_class, sino faux
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
