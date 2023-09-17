class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name):
        print("Urodził się nowy zwierzak!")
        self.__name = name

    @property #pośredni dostęp do atrybutu prywatnego __name
    # wlasciwosc ma taka sama nazwe jak prywatny atrybut
    # dostęp w trybie odczytu do prywatnego atrybutu
    def name(self):
        return self.__name

    @name.setter
    # Umożliwia dostęp w trybie zapisu, z pewnymi ograniczeniami, do prywatnego atrybutu __name poprzez właściwość name:
    def name(self, new_name):
        if new_name == "":
            print("Pusty łańcuch znaków nie może być imieniem zwierzaka.")

        else:
            self.__name = new_name
            print("Zmiana imienia się powiodła.")

    def talk(self):
        print("\nCześć! Jestem", self.name)

# main
crit = Critter("Reksio")
crit.talk()
print(crit.name)
print("\nPróbuję zmienić imię mojego zwierzaka na Pucek...")
crit.name = "Pucek"
print(crit.name)
print("\nPróbuję zmienić imię mojego zwierzaka na pusty łańcuch znaków...")
crit.name = ""
print(crit.name)