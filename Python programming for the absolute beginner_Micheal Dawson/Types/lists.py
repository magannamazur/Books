# mutowalne, mozna zmieniac a i tak beda miec to samo miejsce w pamieci
# mają te funkcje co krotki

lista = [] # pusta lista

inventory = ["miecz", "zbroja", "tarcza", "napój uzdrawiający"]
print("Elementy Twojego inwentarza:")
for item in inventory:
    print(item)

# wyświetl długość listy
print("Twój dobytek zawiera", len(inventory), "elementy.")

# sprawdź, czy element należy do listy, za pomocą operatora in
if "napój uzdrawiający" in inventory:
    print("Należy")

# wyświetl jeden element wskazany przez indeks
index = 2
print("Pod indeksem", index, "znajduje się", inventory[index])

# wyświetl wycinek
start = 0
finish = 2
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

# dokonaj konkatenacji dwóch list
chest = ["złoto", "klejnoty"]
inventory += chest
print("Twój aktualny inwentarz to:")
print(inventory)


################
# TYLKO DLA LIST

# Przypisanie elementowi listy nowej wartości poprzez indeks
inventory[0] = "kusza"
print("Twój aktualny inwentarz z kuszą:")
print(inventory)

# Przypisanie nowej wartości wycinkowi listy
inventory[4:6] = ["kula do wróżenia"] # 4 = kula do wróżenia, 5 = brak, usuwamy
print("Twój aktualny inwentarz to:")
print(inventory)

# Usunięcie elementu listy
del inventory[2]
print("Twój aktualny inwentarz to:")
print(inventory)

# Usunięcie wycinka listy
del inventory[:2]
print("Twój aktualny inwentarz to:")
print(inventory)



##############
# METODY LISTY

# dodawanie ostatniego elementu listy
scores = []
scores.append(5)
print(scores)


# usuniecie wystepujacego elementu
# Metoda remove() usuwa 1 wystepujacy element na podstawie jego wartości
scores.remove(5)
print(scores)
# jesli nie bedzie elementu na liscie pojawi sie błąd
# bezpieczny sposób używania tej metody:
score = 7
if score in scores:
    scores.remove(score)

scores = [1,3,5,7,5,3,2,5]

# Sortowanie wyników
scores.sort(reverse=True) # True dl reverse odwraca kolejność
print(scores)

# liczenie elementów
c = scores.count(5)
print(c)

# numer pozycji pierwszego wystąpienia argumentu wartość
s = scores.index(5)
print(s)

# Wstawia wartość na pozycji i insert(i, wartość)
scores.insert(1, 50)
print(scores)

# Zwraca wartość zajmującą pozycję i oraz usuwa ją z listy. Przekazanie
# numeru pozycji i jest opcjonalne. Jeśli argument i nie zostanie
# podany, usuwany i zwracany jest ostatni element listy.
scores.pop()
print(scores)
scores.pop(1)
print(scores)


# tworzenie nowej zmiennej (jako kopi) poprzez wycinanie - nie zmienia głównej listy
print(scores)
dif_scores = scores[:3]
print(dif_scores, "\t" , scores)


