# atrybut klasy - pojedyncza wartosc zwiazana z sama klasa
# metoda statyczna - metoda zwiazana z klasa a nie obiektem

# Demonstruje atrybuty klasy i metody statyczne
class Critter(object):
    """Wirtualny pupil"""
    # tworzenie atrybutu klasy
    total = 0

    @staticmethod # dekorator
    # bez self, self odwoluje sie do obiektu, a tutaj mamy metode klasy
    def status():
        print("\nOgólna liczba zwierzaków wynosi", Critter.total)

    def __init__(self, name):
        print("Urodził się zwierzak!")
        self.name = name
        Critter.total += 1

#część główna
print("Uzyskanie dostępu do atrybutu klasy Critter.total:", end=" ")
print(Critter.total)
print("\nTworzenie zwierzaków.")
crit1 = Critter("zwierzak 1")
crit2 = Critter("zwierzak 2")
crit3 = Critter("zwierzak 3")
Critter.status()
print("\nUzyskanie dostępu do atrybutu klasy poprzez obiekt:", end= " ")
print(crit1.total)
# Można odczytać wartość atrybutu klasy, wykorzystując dowolny obiekt, który
# należy do tej klasy. Więc mógłbym użyć instrukcji print(crit2.total) lub
# print(crit3.total) i otrzymałbym w tym przypadku taki sam wynik.

# Chociaż możesz wykorzystać obiekt określonej klasy do uzyskania dostępu do
# atrybutu klasy, nie możesz przypisać nowej wartości do atrybutu klasy poprzez
# obiekt. Jeśli chcesz zmienić wartość atrybutu klasy, uzyskaj do niego dostęp
# poprzez nazwę klasy.
crit3.total = 5
print(crit3.total)
print(Critter.total)
print(crit1.total)