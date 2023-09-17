print("Witaj w systemie firmy Bezpieczny Komputer SA")
print("-- bezpieczeństwo to podstawa naszego działania\n")
password = input("Wprowadź hasło: ")
if password == "sekret":
    print("Dostęp został udzielony")

# nie można porównać łańcucha znaków do liczby

print("Witaj w systemie firmy Bezpieczny Komputer SA")
print("-- bezpieczeństwo to podstawa naszego działania\n")
password = input("Wprowadź hasło: " )
if password == "sekret":
    print("Dostęp został udzielony")
else:
    print("Odmowa dostępu")


import random
print("Wyczuwam Twoją energię. Twoje prawdziwe emocje znajdują odbicie na moim ekranie.")
print("Jesteś...")
mood = random.randint(1, 3)
if mood == 1:
    print("szczęśliwy")
elif mood == 2:
    print("obojętny")
elif mood == 3:
    print("smutny")
else:
    print("Nieprawidłowa wartość nastroju! (Musisz być naprawdę w złym humorze).")
print("...dzisiaj.")