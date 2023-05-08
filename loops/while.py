print("\tWitaj w 'Symulatorze trzylatka'\n")
print("Ten program symuluje rozmowę z trzyletnim dzieckiem.")
print("Spróbuj przerwać to szaleństwo.\n")
response = ""
while response != "Dlatego.":
    response = input("Dlaczego?\n")
print("Aha, już wiem.")


# umyślna nieskończona petla

count = 0
while True:
    count += 1
    # zakończ pętlę, jeśli wartość zmiennej count jest większa niż 10
    if count > 10:
        break
    # pomiń liczbę 5
    if count == 5:
        continue
    print(count)


# break - przerywa pętlę
# continue - wraca na początek pętli

print("\tEkskluzywna Sieć Komputerowa")
print("\t Tylko dla członków!\n")
security = 0
username = ""
while not username:
    username = input("Użytkownik: ")
    password = ""
while not password:
    password = input("Hasło: ")
if username == "M.Dawson" and password == "sekret":
    print("Cześć, Mike!")
    security = 5
elif username == "S.Meier" and password == "cywilizacja":
    print("Hej, Sid!")
    security = 3
elif username == "gość" or password == "gość":
    print("Witaj, Gościu!")
    security = 1
else:
    print("Nieudana próba logowania. Nie jesteś taki wyjątkowy.\n")

# not - nie, True gdy warunek False
# and - i, True, gdy oba warunki są True
# or - albo, False, gdy oba warunki są False