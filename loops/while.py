print("\tWitaj w 'Symulatorze trzylatka'\n")
print("Ten program symuluje rozmowę z trzyletnim dzieckiem.")
print("Spróbuj przerwać to szaleństwo.\n")
response = ""
while response != "Dlatego.":
    response = input("Dlaczego?\n")
print("Aha, już wiem.")
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")


# umyślna nieskończona petla

count = 0
while True:
    count += 1
    # zakończ pętlę, jeśli wartość zmiennej count jest większa niż 10
    if count > 10:
        break
    # pomiń liczbę 5
    if count == 5:
        continue
    print(count)
input("\n\nAby zakończyć program, naciśnij klawisz Enter.")