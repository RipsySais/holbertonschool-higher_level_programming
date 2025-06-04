class Student:
    """
    Classe représentant un étudiant avec un prénom, un nom et un âge.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de la classe Student.
        
        :param first_name: Le prénom de l'étudiant.
        :param last_name: Le nom de famille de l'étudiant.
        :param age: L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retourne une représentation sous forme de dictionnaire de l'étudiant.
        
        :return: Un dictionnaire contenant les attributs de l'étudiant.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }

# Exemple d'utilisation :
student1 = Student("John", "Doe", 23)
student2 = Student("Bob", "Smith", 27)
