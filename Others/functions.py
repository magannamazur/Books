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

# dostep funkcji do zmiennej globalnej
# Globalny zasięg
# Demonstruje zmienne globalne
def read_global():
    print("Wartość zmiennej value odczytana z funkcji read_global() wynosi:", value)

def shadow_global():
    value = -10
    print("Wartość zmiennej value odczytana z funkcji shadow_global() wynosi:", value)

def change_global():
    # global - uzyskuje całkowity dostęp do zmiennej globalnej
    global value
    value = -10
    print("Wartość zmiennej value odczytana z funkcji change_global() wynosi:", value)

# główna część programu
# value jest zmienną globalną, ponieważ jesteśmy teraz w zakresie globalnym
value = 10
read_global()
print("Wartość zmiennej globalnej value nadal wynosi:", value,"\n")
shadow_global()
print("Wartość zmiennej globalnej value nadal wynosi:", value,"\n")
change_global()
print("Po powrocie do zakresu globalnego okazuje się, że wartość zmiennej value zmieniła się na:", value)