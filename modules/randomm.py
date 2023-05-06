import random

# generuj liczby losowe z zakresu 1 - 6
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1 # liczbę całkowitą z przedziału od 0 do górnej granicy z jej wyłączeniem

print(die1, die2)