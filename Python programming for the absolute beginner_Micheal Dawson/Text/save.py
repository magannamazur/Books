print("Utworzenie pliku tekstowego za pomocą metody write().")
text_file = open("zapisz_to.txt", "w") # tworzy nowy plik,  jesli wczesniej nie istniał
# jeśli istniał - zawartość zostanie uunięta

# Zapisywanie łańcuchów znaków do pliku
text_file.write("Wiersz 1\n")
text_file.write("To jest wiersz 2\n")
text_file.write("Ten tekst tworzy wiersz 3\n")

text_file.close()


# Zapisywanie listy łańcuchów do pliku

print("\nUtworzenie pliku tekstowego za pomocą metody writelines().")
text_file = open("zapisz_to.txt", "w")
lines = ["Wiersz 1\n",
        "To jest wiersz 2\n",
        "Ten tekst tworzy wiersz 3\n"]
text_file.writelines(lines)