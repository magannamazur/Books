import random

# generuj liczby losowe z zakresu 1 - 6
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1 # liczbę całkowitą z przedziału od 0 do górnej granicy z jej wyłączeniem
die3 = random.randrange(5,7) # dostepne 5,6

print(die1, die2, die3)