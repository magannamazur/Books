class Player(object):
    """ Uczestnik gry. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep

    def ask_yes_no(question):
        """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
        response = None
        while response not in ("t", "n"):
            response = input(question).lower()
        return response

    @staticmethod
    def ask_number(question, low, high):
        """Poproś o podanie liczby z określonego zakresu."""
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

    if __name__ == "__main__":
        print("Uruchomiłeś ten moduł bezpośrednio (zamiast go zaimportować).")
        input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
    # koncepcja zwiazana z modulami, jesli modul zostal uruchomiony warunek jest prawdziwy
    # Natomiast jest fałszywy, jeśli plik został zaimportowany jako moduł.
    # It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module