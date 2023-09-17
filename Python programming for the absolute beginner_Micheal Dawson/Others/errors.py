# try/except bez specyfikacji error type jest niebezpieczne
try:
    num = float(input("Wprowadź liczbę: "))
except:
    print("Wystąpił jakiś błąd!") # jesli nie przejdzie pozytywnie TRY

# Klauzula except umożliwia dokładne określenie typu wyjątków

# specyfikacja typu wyjątku
try:
    num = float(input("\nWprowadź liczbę: "))
except ValueError:
    print("To nie była liczba!")

# obsłuż kilka typów wyjątków
print()
for value in (None, "Hej!"):
    try:
        print("Próba konwersji:", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Wystąpił jakiś błąd!")

# to samo, ale osobna obsługa wyjątkow
print()
for value in (None, "Hej!"):
    try:
        print("Próba konwersji:", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Możliwa jest tylko konwersja łańcucha lub liczby!")
    except ValueError:
        print("Możliwa jest tylko konwersja łańcucha cyfr!")


# pobierz argument wyjątku
try:
    num = float(input("\nWprowadź liczbę: "))
except ValueError as e:
    print("To nie była liczba! Lub wyrażając to na sposób Pythona...")
    print(e)

# try/except/else
# Instrukcje bloku else są wykonywane tylko wtedy, gdy w bloku try nie zostanie zgłoszony żaden wyjątek
try:
    num = float(input("\nWprowadź liczbę: "))
except ValueError:
    print("To nie była liczba!")
else:
    print("Wprowadziłeś liczbę", num)