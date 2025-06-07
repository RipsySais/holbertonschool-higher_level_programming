#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Créer un objet
obj = CustomObject(name="John", age=25, is_student=True)
print("Objet original :")
obj.display()

# Sérialisation
obj.serialize("object.pkl")

# Désérialisation
new_obj = CustomObject.deserialize("object.pkl")
print("\nObjet désérialisé :")
if new_obj:
    new_obj.display()
else:
    print("Erreur de désérialisation.")
