class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name):
        print("Urodził się nowy zwierzak!")
        self.name = name

# reprezentacja obiektu
# bez zmiany byloby cos w stylu: <__main__.Critter object at 0x00A0BA90>
    def __str__(self):
        rep = "Obiekt klasy Critter\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("Cześć! Jestem", self.name, "\n")

# część główna
crit1 = Critter("Reksio")
crit1.talk()
crit2 = Critter("Pucek")
crit2.talk()
print("Wyświetlenie obiektu crit1:")
print(crit1)
print("Bezpośrednie wyświetlenie wartości atrybutu crit1.name:")
print(crit1.name)
crit1.name ="czange"
print(crit1)