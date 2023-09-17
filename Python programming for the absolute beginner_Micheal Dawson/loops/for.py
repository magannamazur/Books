# Pętla for powtarza wykonywanie instrukcji tworzących jej ciało dla każdego elementu sekwencji po kolei

word = input("Wprowadź jakieś słowo: ")
print("\nOto poszczególne litery Twojego słowa:")
for letter in word:
    print(letter)

print("Liczenie:")
# od 0 do 9
for i in range(10):
    print(i, end=" ")

print("\n\nLiczenie co pięć:")
# od 0 do 49 co 5
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nLiczenie do tyłu:")
# od 10 do 1
for i in range(10, 0, -1):
    print(i, end=" ")

import random
word = "indeks"
print("Wartość zmiennej word to: ", word, "\n")
high = len(word)
low = -len(word)
for i in range(10):
    position = random.randrange(low, high) # od -6 włącznie do 6 niewłącznie
    print("word[", position, "]\t", word[position])