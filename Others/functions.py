# łańcuch dokomentujący, docstring
def instructions():
    """Wyświetl instrukcję gry."""
    print("Witaj w największym intelektualnym wyzwaniu wszech czasów")

# wywołanie funkcji
instructions()

# Pobierz i zwróć
def ask_yes_no(question):  # question - parametr
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""

    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

# main
answer = ask_yes_no("\nProszę wprowadzić 't' lub 'n': ") # argument dostarczony funkcji
print("Dziękuję za wprowadzenie:", answer)

# hermetyzacja - żadna zmienna, którą utworzysz w funkcji, nie jest bezpośrednio dostępna na zewnątrz niej samej

# parametry pozycyjne
def birthday1(name, age):
    print("Szczęśliwych urodzin,", name, "!", " Masz już", age, "lat.\n")

# parametry z wartościami domyślnymi
def birthday2(name = "Janusz", age = 5):
    print("Szczęśliwych urodzin,", name, "!", " Masz już", age, "lat.\n")

birthday1("Janusz", 5)
birthday1(5, "Janusz")
birthday1(name = "Janusz", age = 5)
birthday1(age = 5, name = "Janusz")
birthday2()
birthday2(name = "Katarzyna")
birthday2(age = 12)
birthday2(name = "Katarzyna", age = 12)
birthday2("Katarzyna", 12)

# zmienna lokalna - w funkcji
# zmienna globalna - poza funkcją