#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """
    Récupère tous les posts depuis JSONPlaceholder
    et affiche le code statut et les titres des posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()  # Parse JSON en liste de dicts
        for post in posts:
            print(post['title'])
    else:
        print("Erreur lors de la récupération des posts")


def fetch_and_save_posts():
    """
    Récupère tous les posts depuis JSONPlaceholder
    et sauvegarde les données dans un fichier CSV 'posts.csv'.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Ouvre le fichier CSV en mode écriture
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # Écrit la ligne des en-têtes

            # Écrit chaque post comme une ligne dans le CSV
            for post in posts:
                writer.writerow({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
    else:
        print("Erreur lors de la récupération des posts")


# Si ce fichier est exécuté directement, lance les deux fonctions
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
