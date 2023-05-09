# metody łańcuchów
# niemutowalne
# Cytat z wypowiedzi prezesa IBM, Thomasa Watsona, z 1943 r.
quote = "Myślę, że istnieje światowy rynek dla może pięciu komputerów."
print("Oryginalny cytat w tłumaczeniu na język polski:")
print(quote)
print("\nDużymi literami:")
print(quote.upper())
print("\nMałymi literami:")
print(quote.lower())
print("\nWszystkie wyrazy od dużej litery:")
print(quote.title())
print("\nZ drobną zamianą:")
print(quote.replace("pięciu", "milionów"))
print("\nOryginalny cytat pozostał bez zmian:")
print(quote)
print()
#other
print(quote.swapcase())
print(quote.capitalize())
# Zwraca łańcuch, w którym wszystkie białe znaki (tabulatory, spacje
# i znaki nowego wiersza) znajdujące się na początku i na końcu zostały usunięte.
print(quote.strip())
# Zwraca łańcuch, w którym wszystkie wystąpienia łańcucha stary zostały zastąpione łańcuchem nowy.
# Opcjonalny parametr max ogranicza liczbę zamian.
print(quote.replace("e", "E", 3))

word = "Something"
print(len(word))
print(len("ds"))

# indeksowanie od 0
print("word[", 3, "]\t", word[3])
print("word[ 2:4 ]\t", word[2:4])  # 2=m, 3=e, 4 jest wylaczone
print("word[ 0:4 ]\t", word[:4])  # 0=S, 1=o, 2=m, 3=e, 4 jest wylaczone
print("word[ : ]\t", word[:])  # all


# None daje wartość False, ma type NoneType
sth = None
print(type(sth))