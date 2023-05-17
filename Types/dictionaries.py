#pary danych

dic = {}
print(type(dic))

# klucz : wartość

powitanie= {1:"hej", 2: "siema"}
print(powitanie)

# Użycie klucza do pobrania wartości
print(powitanie[1])

# Sprawdzanie klucza za pomocą operatora in przed pobraniem wartości
if 2 in powitanie:
    print(powitanie[2])
else:
    print("Nie mam pojęcia, co to jest 2.")

# Użycie metody get() do pobrania wartości, drugi człon obsługuje błąd braku klucza, wartosc domyslna = NONE
print(powitanie.get(3, "Nie ma takiego klucza."))
print(powitanie.get(3))

# Dodanie pary klucz-wartość
powitanie[5] = "dzien dobry"
powitanie["4a"] = "dzien doberek"
print(powitanie)

# nadpisuje, bo uzyty klucz już istnieje
powitanie["4a"] = "hahhha"
print(powitanie)

# zabezpieczenie dodania
klucz = 5
if klucz not in powitanie:
    powitanie[5] = "dzien dobry"
else:
    print("klucz jest już użyty")