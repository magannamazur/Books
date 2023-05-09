# krotka
# niemutowalna
krotka = () # wartosc False
print(type(krotka))

if not krotka: # not False = True
    print("Krotka jest pusta.")

inventory = ("miecz",
"zbroja",
"tarcza",
"napój uzdrawiający")
for item in inventory:
    print(item)

# długoś len()
print("Twój dobytek zawiera", len(inventory), "elementy.")

# sprawdzanie konkretnego elementu
if "napój uzdrawiający" in inventory:
    print("Dożyjesz dnia, w którym stoczysz walkę.")

# indeksowanie
index = 2
print("Pod indeksem", index, "znajduje się", inventory[index]) # liczone od 0

# wycinanie
start = 0
finish = 2
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

# Konkatenacja krotek
chest = ("złoto", "klejnoty")
print(id(inventory))
inventory += chest
print("Twój aktualny inwentarz to:")
print(inventory)
print(id(inventory))