def dodaj(a, b):
    """Dodaj dwie liczby."""
    return a + b


def odejmij(a, b):
    """Odejmij drugą liczbę od pierwszej."""
    return a - b


def pomnoz(a, b):
    """Pomnóż dwie liczby."""
    return a * b


def podziel(a, b):
    """Podziel pierwszą liczbę przez drugą."""
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a / b


# Słownik operatorów
OPERATORY = {
    "+": dodaj,
    "-": odejmij,
    "*": pomnoz,
    "/": podziel,
}


def pobranie_liczby(komunikat):
    """Pobierz liczbę od użytkownika z obsługą błędów."""
    while True:
        try:
            return float(input(komunikat))
        except ValueError:
            print("Błąd: Wprowadź prawidłową liczbę!")


def main():
    """Główna funkcja kalkulatora."""
    print("\n=== Kalkulator ===")
    
    while True:
        try:
            a = pobranie_liczby("Podaj pierwszą liczbę: ")
            b = pobranie_liczby("Podaj drugą liczbę: ")
            operator = input("Podaj operator (+, -, *, /): ").strip()
            
            if operator not in OPERATORY:
                print("Błąd: Nieznany operator!")
                continue
            
            wynik = OPERATORY[operator](a, b)
            print(f"{a} {operator} {b} = {wynik}\n")
            
        except ValueError as e:
            print(f"Błąd: {e}\n")
        
        if input("Chcesz wykonać kolejne obliczenie? (t/n): ").lower() != "t":
            print("Do widzenia!")
            break


if __name__ == "__main__":
    main() 
