#!/usr/bin/python3
def say_my_name(prenom, nom=""):
    """
    Affiche "Je m'appelle <prenom> <nom>".

    Arguments:
    prenom -- prenom, doit etre une chaine de caracteres
    nom -- nom, doit etre une chaine de caracteres (optionnel)

    Exceptions:
    TypeError -- si prenom ou nom ne sont pas des chaines de caracteres
    """
    if not isinstance(prenom, str):
        raise TypeError("Le prenom doit etre une chaine de caracteres")
    if not isinstance(nom, str):
        raise TypeError("Le nom doit etre une chaine de caracteres")

    if nom:
        print(f"Je m'appelle {prenom} {nom}")
    else:
        print(f"Je m'appelle {prenom}")
