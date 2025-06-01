class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"[{item}] a été ajouté à la liste.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extension de la liste avec {len(iterable)} éléments.")

    def remove(self, item):
        if item in self:
            print(f"[{item}] a été supprimé de la liste.")
            super().remove(item)
        else:
            print(
                f"Impossible de supprimer [{item}]: "
                "l'élément n'est pas dans la liste."
            )

    def pop(self, index=-1):
        if len(self) > 0:
            item = self[index]
            print(f"[{item}] a été supprimé de la liste.")
            return super().pop(index)
        else:
            print("Impossible de supprimer un élément : la liste est vide.")
