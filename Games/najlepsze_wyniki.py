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

# wyświetl tabelę najlepszych wyników
    elif choice == "1":
        print("Najlepsze wyniki\n")
        print("GRACZ\tWYNIK")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

# add a score
    elif choice == "2":
        name = input("Podaj nazwę gracza: ")
        score = int(input("Jaki wynik gracz uzyskał?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]  # zachowaj tylko 5 najlepszych wyników