#!/usr/bin/env python3
"""
Script qui liste tous les états de la base de données hbtn_0e_0_usa
triés par id croissant
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Connexion à la base de données
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name
        )

        # Création du curseur
        cursor = db.cursor()

        # Exécution de la requête
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Récupération et affichage des résultats
        for state in cursor.fetchall():
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)

    finally:
        # Fermeture de la connexion
        if 'db' in locals():
            db.close()
