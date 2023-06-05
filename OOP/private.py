# Demonstruje zmienne i metody prywatne
class Critter(object):
    """Wirtualny pupil"""
    def __init__(self, name, mood):
        print("Urodził się nowy zwierzak!")
        self.name = name  # atrybut publiczny
        self.__mood = mood  # atrybut prywatny

    def talk(self):
        print("\nJestem", self.name)
        print("W tej chwili czuję się", self.__mood, "\n")

    def __private_method(self):
        print("To jest metoda prywatna.")

# Jest to metoda prywatna, lecz każda z pozostałych metod klasy ma do niej łatwy dostęp.

    def public_method(self):
        print("To jest metoda publiczna.")
        self.__private_method()

crit = Critter(name = "Reksio", mood = "szczęśliwy") # wywola metode init
print(crit)
print(crit.name)
print(crit.talk())
print(crit._Critter__mood) # wyswietli mood
# print(crit.mood) # AttributeError
print(crit.public_method())
print(crit._Critter__private_method()) # da dostep do publicznej metody