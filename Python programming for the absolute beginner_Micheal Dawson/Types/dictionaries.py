# mutowalne, maja po zmianie to samo miejsce w pamiecie
# pary danych
# klucz jest: niemutowalny (zeby nie zmienic klucza), unikalny
# wartość: obojętnie, może się powtarzać

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

# zabezpieczenie dodania (teZ spoko przy usuwaniu, żeby uniknąć błędu)
klucz = 5
if klucz not in powitanie:
    powitanie[5] = "dzien dobry"
else:
    print("klucz jest już użyty")

# Usunięcie pary klucz-wartość
del powitanie[5]
print(powitanie)

# keys() - zwraca widok wszystkich kluczy występujących w słowniku
print(powitanie.keys())

# values() - zwraca widok wszystkich wartości występujących w słowniku
print(powitanie.values())

# items() - zwraca widok wszystkich elementów słownika, każdy element to dwuskładnikowa krotka (klucz, wartość)
print(powitanie.items())

# keys(), values() i items() — są pod pewnymi względami podobne do list. Można po nich iterować za pomocą pętli for.