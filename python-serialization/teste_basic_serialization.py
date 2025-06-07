#!/usr/bin/env python3
from task_00_basic_serialization import (
    serialize_and_save_to_file,
    load_and_deserialize
)

# Exemple de données à sérialiser
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Sérialiser les données dans un fichier JSON
serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Données sérialisées et enregistrées dans 'data.json'.")

# Charger les données depuis le fichier JSON
deserialized_data = load_and_deserialize('data.json')
print("Données désérialisées :")
print(deserialized_data)
