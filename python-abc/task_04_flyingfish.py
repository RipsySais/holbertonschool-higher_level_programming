class Fish:
    def swim(self):
        print("Le poisson nage")

    def habitat(self):
        print("Le poisson vit dans l'eau")


class Bird:
    def fly(self):
        print("L'oiseau vole")

    def habitat(self):
        print("L'oiseau vit dans le ciel")


class FlyingFish(Fish, Bird):
    def swim(self):
        print("Le poisson volant nage !")

    def fly(self):
        print("Le poisson volant s'envole !")

    def habitat(self):
        print("Le poisson volant vit à la fois dans l'eau et dans le ciel")
