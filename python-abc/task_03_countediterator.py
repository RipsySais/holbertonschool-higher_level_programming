class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        try:
            item = next(self.iterator)  # Récupérer l'élément suivant
            self.count += 1  # Incrémenter le compteur
            return item
        except StopIteration:
            raise StopIteration("Plus d'éléments.")

    def get_count(self):
        return self.count

    def __iter__(self):
        return self  # L'itérateur doit retourner lui-même

# Tests
data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)
