#!/usr/bin/env python3
"""
Fichier de test pour task_00_basic_serialization.py
"""

from task_00_basic_serialization import load_and_deserialize,
serialize_and_save_to_file

# Exemple de données à sérialiser
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Nom du fichier de test
filename = 'data.json'

# Sérialiser les données au format JSON et les enregistrer dans un fichier
serialize_and_save_to_file(data_to_serialize, filename)
print("Données sérialisées et enregistrées dans 'data.json'.")

# Charger et désérialiser les données depuis 'data.json'
deserialized_data = load_and_deserialize(filename)
print("Données désérialisées :")
print(deserialized_data)
