print("Otwarcie i zamknięcie pliku.")
# brak ścieżki, python szuka w bieżacym katalogu
text_file = open("odczytaj_to.txt", "r")
text_file.close()


# "r" Odczyt danych. Jeśli plik nie istnieje, Python zasygnalizuje błąd.
# "w" Zapis danych. Jeśli plik już istnieje, jego zawartość zostaje zastąpiona przez nowe dane. Jeśli nie istnieje, zostaje utworzony.
# "a" Dopisanie danych na końcu pliku tekstowego. Jeśli plik istnieje, nowe dane  zostają do niego dopisane. Jeśli plik nie istnieje, jest tworzony.
# "r+" Odczyt i zapis danych z (do) pliku tekstowego. Jeśli plik nie istnieje, Python zasygnalizuje błąd.
# "w+" Zapis i odczyt danych do (z) pliku tekstowego. Jeśli plik istnieje, jego zawartość zostanie zastąpiona nowymi danymi. Jeśli nie istnieje, zostanie utworzony.
# "a+" Dopisywanie i odczyt danych do (z) pliku tekstowego. Jeśli plik istnieje, nowe dane są dopisywane na jego końcu. Jeśli plik nie istnieje, zostanie utworzony.



print("\nOdczytywanie znaków z pliku.")
text_file = open("odczytaj_to.txt", "r")
print(text_file.read(1))
print(text_file.read(9)) # jako znak liczy przejście do nowej lini
text_file.close()


print("\nOdczytanie całego pliku za jednym razem.")
text_file = open("odczytaj_to.txt", "r")
whole_thing = text_file.read() # bez podania liczby znaków
print(whole_thing)
text_file.close()


print("\nOdczytywanie znaków z wiersza.")
text_file = open("odczytaj_to.txt", "r")
print(text_file.readline(1))
print(text_file.readline(7)) # odczytuje z BIEŻĄCEGO wierza
text_file.close()


print("\nOdczytywanie po jednym wierszu na raz.")
text_file = open("odczytaj_to.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()


print("\nWczytanie całego pliku do listy po wierszu")
text_file = open("odczytaj_to.txt", "r")
lines = text_file.readlines() # łańcuch znaków staje się elementem listy
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()


print("\nPobieranie zawartości pliku wiersz po wierszu przy użyciu pętli.")
text_file = open("odczytaj_to.txt", "r")
for line in text_file:
    print(line)
text_file.close()