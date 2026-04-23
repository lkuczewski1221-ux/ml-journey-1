# ============================================
# DZIEŃ 1 - PODSTAWY PYTHONA
# Python 3.14.4 - Perfect for AI/ML!
# ============================================

import sys
        
print(f"Python wersja: {sys.version}")
print(f"Python wersja (krótka): {sys.version_info.major}.{sys.version_info.minor}")
print()

# 1. WYŚWIETLANIE TEKSTU
print("Hello World!")
print("Witaj w świecie Pythona!")

# 2. ZMIENNE I TYPY DANYCH
imie = "Jan"
wiek = 25
wzrost = 175.5
czy_programuje = True

print(f"\nImię: {imie}")
print(f"Wiek: {wiek}")
print(f"Wzrost: {wzrost} cm")
print(f"Czy programuje: {czy_programuje}")

# 3. OPERACJE MATEMATYCZNE
a = 10
b = 3

print(f"\n{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")  # dzielenie całkowite
print(f"{a} % {b} = {a % b}")    # reszta z dzielenia
print(f"{a} ** {b} = {a ** b}")  # potęga

# 4. LISTY
zwierzęta = ["kot", "pies", "słoń"]
print(f"\nZwierzęta: {zwierzęta}")
print(f"Pierwsze: {zwierzęta[0]}")
print(f"Ostatnie: {zwierzęta[-1]}")

zwierzęta.append("ptak")
print(f"Po dodaniu: {zwierzęta}")

# 5. SŁOWNIKI
osoba = {
    "imie": "Jan",
    "wiek": 25,
    "miasto": "Warszawa"
}

print(f"\nOsoba: {osoba}")
print(f"Imię: {osoba['imie']}")
print(f"Wiek: {osoba['wiek']}")

# 6. WARUNKI
wiek_uzytkownika = 20

if wiek_uzytkownika >= 18:
    print("\nJesteś pełnoletni!")
else:
    print("\nJesteś niepełnoletni!")

# 7. PĘTLE
print("\nLiczby od 1 do 5:")
for i in range(1, 6):
    print(f"  {i}")

print("\nLiczby od 5 do 1:")
for i in range(5, 0, -1):
    print(f"  {i}")

# 8. FUNKCJE
def powitaj(imie):
    """Funkcja witająca"""
    return f"Cześć, {imie}!"

print(f"\n{powitaj('Anna')}")
print(f"{powitaj('Adam')}")

# 9. WŁASNA FUNKCJA - KALKULATOR
def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    """
    Dzieli a przez b.

    Args:
        a (float): Licznik.
        b (float): Mianownik.

    Returns:
        float: Wynik dzielenia jeśli b != 0.
        str: Komunikat o błędzie jeśli b == 0.
    """
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"

print(f"\nKalkulator:")
print(f"5 + 3 = {dodaj(5, 3)}")
print(f"5 - 3 = {odejmij(5, 3)}")
print(f"5 * 3 = {pomnoz(5, 3)}")
wynik_podziel = podziel(5, 3)
if wynik_podziel is not None:
    print(f"5 / 3 = {wynik_podziel}")
else:
    print("5 / 3 = Nie można dzielić przez zero!")

# ============================================
# ZADANIE DOMOWE - WYKONAJ SAM!
# ============================================

print("\n" + "="*40)
print("ZADANIE DOMOWE - WYKONAJ SAM!")
print("="*40)
print("""
1. Stwórz zmienną "miasto" i wydrukujej
2. Stwórz listę z 3 Twoimi ulubionymi jedzeniami
3. Stwórz słownik z danymi o sobie (imie, wiek, miasto, hobby)
4. Napisz funkcję która powie Ci ile masz lat w miesiącach
5. Napisz program który pyta o imię i wiek, a potem wyświetla powitanie
""")

miasto = "Warszawa"
print(f"\nMiasto: {miasto}")
jedzenie = ["stek", "pizza", "szpargi"]
print(f"\nJedzenie: {jedzenie}")

osoba = {
    "imie": "Stefan",
    "wiek": 36,
    "miasto": "Warszawa",
    "hobby": "Szukanie fazy"
}

def wiek_w_miesiacach(lata):
    miesiace = lata * 12
    return miesiace

print(f"\nWiek w miesiącach (36 lat): {wiek_w_miesiacach(36)}")

imie = input("\nPodaj swoje imię: ")
wiek = int(input("Podaj swój wiek: "))
print(f"\nCześć, {imie}! Masz {wiek} lat. W miesiacach to {wiek_w_miesiacach(wiek)} miesięcy!")

