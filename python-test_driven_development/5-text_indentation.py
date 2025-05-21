#!/usr/bin/python3
def text_indentation(texte):
    """
    Affiche un texte avec 2 nouvelles lignes après '.', '?' et ':'

    Arguments:
    texte -- Le texte à formater (doit être une chaîne)

    Exceptions:
    TypeError -- si texte n'est pas une chaîne
    """

    if not isinstance(texte, str):
        raise TypeError("le texte doit être une chaîne")

    resultat = ""
    i = 0
    while i < len(texte):
        resultat += texte[i]
        if texte[i] in ".?:":
            resultat += "\n\n"
        i += 1

    # Supprimer les espaces inutiles au début et à la fin des lignes
    lignes = [ligne.strip() for ligne in resultat.split("\n")]
    for ligne in lignes:
        if ligne:  # Éviter les lignes vides inutiles
            print(ligne)
