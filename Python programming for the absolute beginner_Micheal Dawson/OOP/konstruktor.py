# Zwierzak z konstruktorem
# Demonstruje konstruktory
class Critter(object):
    """Wirtualny pupil"""
    # metoda __init__
    # jest wywoływana automatycznie przez każdy nowo tworzony obiekt klasy Critter
    # natychmiast po zaistnieniu obiektu

    def __init__(self):  # metoda inicjalizacji = konstruktor
        print("Urodził się nowy zwierzak!")
    def talk(self):
        print("\nCześć! Jestem egzemplarzem klasy Critter.")

# część główna
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()