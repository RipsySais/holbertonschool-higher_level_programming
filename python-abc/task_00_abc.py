from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un animal.
    Cette classe définit une méthode abstraite `sound` que
    toutes les sous-classes doivent implémenter.
    """

    @abstractmethod
    def sound(self):
        """
        Méthode abstraite qui doit être implémentée par les sous-classes.
        Retourne :
            str : Son caractéristique de l'animal.
        """
        pass


class Dog(Animal):
    """
    Classe Dog, représentant un chien, qui hérite de la classe Animal.
    """

    def sound(self):
        """
        Implémentation de la méthode sound pour les chiens.
        Retourne :
            str : "Bark", le son caractéristique d'un chien.
        """
        return "Bark"


class Cat(Animal):
    """
    Classe Cat, représentant un chat, qui hérite de la classe Animal.
    """

    def sound(self):
        """
        Implémentation de la méthode sound pour les chats.
        Retourne :
            str : "Meow", le son caractéristique d'un chat.
        """
        return "Meow"


# Test des classes
if __name__ == "__main__":
    bobby = Dog()
    garfield = Cat()

    print(bobby.sound())    # Affichera "Bark"
    print(garfield.sound())  # Affichera "Meow"
