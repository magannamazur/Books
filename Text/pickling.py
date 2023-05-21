# marynowanie
# zapisywanie w pliku złożonych struktór:
#  liczby,
#  łańcuchy znaków,
#  krotki,
#  listy,
#  słowniki.

import pickle, shelve

print("Marynowanie list.")
variety = ["łagodny", "pikantny", "kwaszony"]
shape = ["cały", "krojony wzdłuż", "w plasterkach"]
brand = ["Dawtona", "Klimex", "Vortumnus"]

# zapis w pliku binarnym, nie tekstowym
f = open("pikle1.dat", "wb")

# "rb" Odczyt danych z pliku binarnego. Jeśli plik nie istnieje, Python zasygnalizuje błąd.
# "wb" Zapis danych do pliku binarnego. Jeśli plik już istnieje, jego zawartość zostaje
# zastąpiona przez nowe dane. Jeśli nie istnieje, zostaje utworzony.
# "ab" Dopisanie danych na końcu pliku binarnego. Jeśli plik istnieje, nowe dane
# zostają do niego dopisane. Jeśli plik nie istnieje, jest tworzony.
# "rb+" Odczyt i zapis danych z (do) pliku binarnego. Jeśli plik nie istnieje, Python
# zasygnalizuje błąd.
# "wb+" Zapis i odczyt danych do (z) pliku binarnego. Jeśli plik istnieje, jego zawartość
# zostanie zastąpiona nowymi danymi. Jeśli nie istnieje, zostanie utworzony.
# "ab+" Dopisywanie i odczyt danych do (z) pliku binarnego. Jeśli plik istnieje, nowe
# dane są dopisywane na jego końcu. Jeśli plik nie istnieje, zostanie utworzony

# dump(dane do zamarynowania = obiekt, plik do ich przechowywania)
pickle.dump(variety, f) # obiekt variety
pickle.dump(shape, f)  # obiekt shape itd.
pickle.dump(brand, f)
f.close()


# Odczytywanie danych z pliku
print("\nOdmarynowanie list.")
f = open("pikle1.dat", "rb")
v = pickle.load(f) # tworzenie obiektu v
shape = pickle.load(f)
brand = pickle.load(f)
print(v)
print(shape)
print(brand)
f.close()

# shelving - umieszczenie „na półce”
# shelve.open(nazwa pliku, tryb = domyslnie c)
print("\nOdkładanie list na półkę.")
s = shelve.open("pikle2.dat")

# "c" Otwórz plik do odczytu i zapisu. Jeśli plik nie istnieje, zostaje utworzony.
# "n" Utwórz nowy plik do odczytu i zapisu. Jeśli plik już istnieje, jego zawartość
# zostaje nadpisana.
# "r" Odczytuj dane z pliku. Jeśli plik nie istnieje, Python zasygnalizuje błąd.
# "w" Zapisuj dane do pliku. Jeśli plik nie istnieje, Python zasygnalizuje błąd.

# zapisanie słownika (klucz = wartości):
# klucz półki może być tylko łańcuchem znaków
s["odmiana"] = ["łagodny", "pikantny", "kwaszony"]
s["kształt"] = ["cały", "krojony wzdłuż", "w plasterkach"]
s["marka"] = ["Dawtona", "Klimex", "Vortumnus"]

s.sync() # upewnij się, że dane zostały zapisane

print("\nPobieranie list z pliku półki:")
print("marka -", s["marka"])
print("kształt -", s["kształt"])
print("odmiana -", s["odmiana"])

s.close()