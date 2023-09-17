class Dog(object):
    """Wirtualny pupil"""
    def talk(self):  # kazda metoda musi zawierac pierwszy parametr self
        print("Cześć! Jestem egzemplarzem klasy Dog.")

# część główna
jamnik = Dog()  # tworzenie obiektu jamnik
jamnik.talk()