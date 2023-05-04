print("Koniec gry")
# print - funkcja
# "Koniec gry" - argument wprowadzony do funkcji
# "Koniec gry" - łańcuch, ciąg znaków - literał
# print("Koniec gry") - instrukcja

# Wypisywanie wielu wartości
print("Taki sam", "komunikat", "jak przedtem,")
# każda wartość jest wypisywana ze spacją w roli separatora, spacja lub enter między wartościami nie mają znaczenia
print("tylko",
"nieco",
"większy.")

# Definiowanie łańcucha końcowego funkcji print
# defaultowo: end='\n'
print("Oto", end=" ")
print("on...")

# Tworzenie łańcuchów w potrójnych cudzysłowach
print("""
_ __ ____ _ _ _____ ______ _____
| |/ / / __ \ | \ | | |_ _| | ____| / ____|
| ' / | | | | | \| | | | | |__ | |
| < | | | | | . ` | | | | __| | |
| . \ | |__| | | |\ | _| |_ | |____ | |____
|_|\_\ \____/ |_| \_| |_____| |______| \_____|
_____ _____ __ __
/ ____| | __ \ \ \ / /
| | __ | |__) | \ \_/ /
| | |_ | | _ / \ /
| |__| | | | \ \ | |
\_____| |_| \_\ |_|
""")

# Używanie sekwencji specjalnych w łańcuchach znaków
# poprzedzone lewym ukośnikiem "\"
print("Koniec \n gry")

# lewy ukośnik elimunuje funkcję cudzysłowia i samego siebie uzyty podwójnie
print("Koniec \"gry\"")
print("\t\t\t \\ \\ \\ \\ \\ \\ \\")

# 3 znaki tabulacji \t\t\t - pomocne w ustawianiu kolumn
print("\t\t\tZabawne podziękowania")

# Wywołanie sygnału dzwonka systemowego - poza IDE
print("\a")

# Konkatenacja łańcuchów
print("Możesz dokonać konkatenacji dwóch " + "łańcuchów za pomocą operatora '+'.")

# lewy ukośnik z plusem \+ może też być znakiem kontynuacji wiersza
print("\nTen łańcuch " + "może nie " + "sprawiać wiel" + "kiego wrażenia. " \
+ "Ale " + "pewnie nie wiesz," + " że jest\n" + "to jeden napraw" )

# Powielanie łańcuchów
print("Lody!" * 10)

# Operacje na liczbach
print("1500 - 45 + 25 =", 1500 - 45 + 25)