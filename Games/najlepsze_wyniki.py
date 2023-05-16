scores = []
choice = None
while choice != "0":
print(
"""
Najlepsze wyniki
0 - zakończ
1 - wyświetl wyniki
2 - dodaj wynik
"""
)
choice = input("Wybierasz: ")
print()
# zakończ
if choice == "0":
print("Do widzenia.")