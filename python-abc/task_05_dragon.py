class SwimMixin:
    def swim(self):
        print("La créature nage !")


class FlyMixin:
    def fly(self):
        print("La créature vole !")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("Le dragon rugit !")
