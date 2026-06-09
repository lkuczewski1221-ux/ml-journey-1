import random


def losowa_liczba(n):
    """Generuj losową liczbę całkowitą od 1 do n (włącznie)."""
    return random.randint(1, n)


def main():
    """Główna funkcja do interakcji z użytkownikiem."""
    print("\n=== Generator Losowych Liczb ===")
    
    try:
        n = int(input("Podaj maksymalną liczbę: "))
        if n < 1:
            print("Błąd: Liczba musi być większa lub równa 1!")
            return
        
        wynik = losowa_liczba(n)
        print(f"Losowa liczba od 1 do {n}: {wynik}\n")
        
    except ValueError:
        print("Błąd: Wprowadź prawidłową liczbę całkowitą!")


if __name__ == "__main__":
    main()
