import random, gra

print("Witaj w najprostszej grze na świecie!\n")
again = None
while again != "n":
    players = []
    num = gra.Player.ask_number(question ="Podaj liczbę graczy (2 - 5): ", low = 2, high = 5)

    for i in range(num):
        name = input("Nazwa gracza: ")
        score = random.randrange(100) + 1
        player = gra.Player(name, score)
        players.append(player)

    print("\nOto wyniki gry:")
    for player in players:
        print(player)

    again = gra.Player.ask_yes_no("\nCzy chcesz zagrać ponownie? (t/n): ")