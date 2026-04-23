# ============================================
# DZIEŃ 2 - ZMIENNE I OPERATORY
# Python 3.14.4 - AI/ML Journey
# ============================================

print("=" * 50)
print("DZIEŃ 2: ZMIENNE I OPERATORY")
print("=" * 50)

# ============================================
# 1. TYPY DANYCH - WIĘCEJ O TYM
# ============================================

print("\n--- TYPY DANYCH ---")

# Liczby całkowite
liczba_cala = 42
print(f"int: {liczba_cala} - typ: {type(liczba_cala)}")

# Liczby zmiennoprzecinkowe
liczba_zmienna = 3.14
print(f"float: {liczba_zmienna} - typ: {type(liczba_zmienna)}")

# Tekst
tekst = "Python AI/ML"
print(f"str: '{tekst}' - typ: {type(tekst)}")

# Wartości logiczne
prawda = True
falsz = False
print(f"bool: {prawda} - typ: {type(prawda)}")

# None (brak wartości)
nic = None
print(f"NoneType: {nic} - typ: {type(nic)}")

# ============================================
# 2. OPERATORY ARYTMETYCZNE - ZAAWANSOWANE
# ============================================

print("\n--- OPERATORY ARYTMETYCZNE ---")

a, b = 15, 4

print(f"{a} + {b} = {a + b}")      # Dodawanie
print(f"{a} - {b} = {a - b}")      # Odejmowanie
print(f"{a} * {b} = {a * b}")      # Mnożenie
print(f"{a} / {b} = {a / b}")      # Dzielenie (float)
print(f"{a} // {b} = {a // b}")    # Dzielenie całkowite
print(f"{a} % {b} = {a % b}")      # Reszta z dzielenia
print(f"{a} ** {b} = {a ** b}")    # Potęga

# Operatory przypisania
x = 10
x += 5   # x = x + 5
print(f"\nx += 5 → x = {x}")

x -= 3   # x = x - 3
print(f"x -= 3 → x = {x}")

x *= 2   # x = x * 2
print(f"x *= 2 → x = {x}")

x /= 2   # x = x / 2
print(f"x /= 2 → x = {x}")

# ============================================
# 3. OPERATORY PORÓWNAŃ
# ============================================

print("\n--- OPERATORY PORÓWNAŃ ---")

x, y = 10, 20

print(f"{x} == {y} → {x == y}")    # Równość
print(f"{x} != {y} → {x != y}")    # Nierówność
print(f"{x} > {y} → {x > y}")      # Większe
print(f"{x} < {y} → {x < y}")      # Mniejsze
print(f"{x} >= {y} → {x >= y}")    # Większe lub równe
print(f"{x} <= {y} → {x <= y}")    # Mniejsze lub równe

# ============================================
# 4. OPERATORY LOGICZNE
# ============================================

print("\n--- OPERATORY LOGICZNE ---")

a, b = True, False

print(f"{a} and {b} → {a and b}")  # I logiczne
print(f"{a} or {b} → {a or b}")    # Lub logiczne
print(f"not {a} → {not a}")        # Negacja

# Operatory z wartościami
wiek = 25
czy_ma_przedluzenie = True

if wiek >= 18 and czy_ma_przedluzenie:
    print("\n✅ Możesz prowadzić samochód!")
else:
    print("\n❌ Nie możesz prowadzić samochodu!")

# ============================================
# 5. KONWERSJA TYPÓW
# ============================================

print("\n--- KONWERSJA TYPÓW ---")

# String na liczbę
tekst_num = "42"
liczba = int(tekst_num)
print(f"'{tekst_num}' → int: {liczba}")

float_num = float("3.14")
print(f"'3.14' → float: {float_num}")

# Liczba na string
tekst_od_liczby = str(100)
print(f"100 → str: '{tekst_od_liczby}'")

# Liczba na bool
print(f"bool(0) → {bool(0)}")
print(f"bool(1) → {bool(1)}")
print(f"bool(42) → {bool(42)}")
print(f"bool('') → {bool('')}")
print(f"bool('tekst') → {bool('tekst')}")

# ============================================
# 6. OPERACJE NA STRINGACH
# ============================================

print("\n--- OPERACJE NA STRINGACH ---")

tekst = "Python AI/ML"

# Długość
print(f"Długość: {len(tekst)}")

# Indeksowanie
print(f"Pierwszy znak: '{tekst[0]}'")
print(f"Ostatni znak: '{tekst[-1]}'")

# Sliceing (wycinki)
print(f"Pierwsze 3 znaki: '{tekst[:3]}'")
print(f"Ostatnie 3 znaki: '{tekst[-3:]}'")
print(f"Środek: '{tekst[0:6]}'")

# Metody stringów
print(f"Wielkie litery: '{tekst.upper()}'")
print(f"Małe litery: '{tekst.lower()}'")
print(f"Zastąp AI/ML Machine Learning: '{tekst.replace('AI/ML', 'Machine Learning')}'")

# Konkatenacja
imie = "Stefan"
miasto = "Warszawa"
print(f"\n'{imie}' + ' mieszka w ' + '{miasto}' = '{imie} mieszka w {miasto}'")

# ============================================
# 7. OPERACJE NA LISTACH
# ============================================

print("\n--- OPERACJE NA LISTACH ---")

liczby = [1, 2, 3, 4, 5]

# Długość
print(f"Długość listy: {len(liczby)}")

# Indeksowanie
print(f"Pierwszy element: {liczby[0]}")
print(f"Ostatni element: {liczby[-1]}")

# Sliceing
print(f"Pierwsze 3 elementy: {liczby[:3]}")
print(f"Elementy od 2 do 4: {liczby[1:4]}")

# Dodawanie
liczby.append(6)
print(f"Po append(6): {liczby}")

liczby.insert(0, 0)
print(f"Po insert(0, 0): {liczby}")

# Usuwanie
liczby.remove(0)
print(f"Po remove(0): {liczby}")

ostatni = liczby.pop()
print(f"Po pop(): {liczby}, usunięto: {ostatni}")

# Sortowanie
fruits = ["banan", "jabłko", "gruszka"]
fruits.sort()
print(f"Posortowane: {fruits}")

fruits.reverse()
print(f"Odwrócone: {fruits}")

# ============================================
# 8. OPERACJE NA SŁOWNIKACH
# ============================================

print("\n--- OPERACJE NA SŁOWNIKACH ---")

osoba = {
    "imie": "Stefan",
    "wiek": 36,
    "miasto": "Warszawa",
    "hobby": ["programowanie", "AI", "ML"]
}

print(f"Osoba: {osoba}")

# Dostęp do wartości
print(f"Imię: {osoba['imie']}")
print(f"Wiek: {osoba['wiek']}")

# Dodawanie
osoba["zawód"] = "Data Scientist"
print(f"Po dodaniu: {osoba}")

# Aktualizacja
osoba["wiek"] = 37
print(f"Po aktualizacji: {osoba}")

# Usuwanie
del osoba["zawód"]
print(f"Po usunięciu: {osoba}")

# Klucze i wartości
print(f"\nKlucze: {osoba.keys()}")
print(f"Wartości: {osoba.values()}")
print(f"Pary klucz-wartość: {osoba.items()}")

# ============================================
# 9. ZMIENNE KROTCE (TUPLE)
# ============================================

print("\n--- KROTCE (TUPLE) ---")

krotka = (1, 2, 3, 4, 5)
print(f"Krotka: {krotka}")
print(f"Pierwszy element: {krotka[0]}")

# Krotki są niezmienne (immutable)
# krotka[0] = 10  # To by dało błąd!

# ============================================
# 10. PĘTLE - WIĘCEJ PRZYKŁADÓW
# ============================================

print("\n--- PĘTLE ---")

# while
licznik = 1
while licznik <= 5:
    print(f"Liczba: {licznik}")
    licznik += 1

# for z enumerate
zwierzęta = ["kot", "pies", "słoń"]
for index, zwierze in enumerate(zwierzęta):
    print(f"{index + 1}. {zwierze}")

# for z range i step
print("\nLiczby co 2 od 0 do 10:")
for i in range(0, 11, 2):
    print(f"  {i}", end=" ")
print()

# ============================================
# 11. FUNKCJE - ZAAWANSOWANE
# ============================================

print("\n--- FUNKCJE ZAAWANSOWANE ---")

# Funkcja z wieloma parametrami
def oblicz_bmi(waga, wzrost):
    """Oblicza BMI"""
    bmi = waga / (wzrost ** 2)
    return round(bmi, 2)

print(f"BMI dla 80kg, 1.80m: {oblicz_bmi(80, 1.80)}")

# Funkcja z parametrami domyślnymi
def powitaj_uzytkownika(imie, powitanie="Cześć"):
    return f"{powitanie}, {imie}!"

print(f"{powitaj_uzytkownika('Anna')}")
print(f"{powitaj_uzytkownika('Adam', 'Witaj')}")

# Funkcja z wieloma zwracanymi wartościami
def statystyki_liczb(liczby):
    return sum(liczby), len(liczby), sum(liczby) / len(liczby)

moje_liczby = [10, 20, 30, 40, 50]
suma, ilosc, srednia = statystyki_liczb(moje_liczby)
print(f"\nLiczby: {moje_liczby}")
print(f"Suma: {suma}, Ilość: {ilosc}, Średnia: {srednia}")

# ============================================
# 12. LISTY KOMPRESYJNE (LIST COMPREHENSIONS)
# ============================================

print("\n--- LISTY KOMPRESYJNE ---")

# Zwykła pętla
kwadraty = []
for i in range(5):
    kwadraty.append(i ** 2)
print(f"Zwykła: {kwadraty}")

# List comprehension
kwadraty2 = [i ** 2 for i in range(5)]
print(f"Comprehension: {kwadraty2}")

# Z warunkiem
parzyste = [i for i in range(10) if i % 2 == 0]
print(f"Parzyste: {parzyste}")

# ============================================
# 13. HANDLOWANIE BŁĘDAMI
# ============================================

print("\n--- HANDLOWANIE BŁĘDAMI ---")

def dziel(a, b):
    try:
        wynik = a / b
        return wynik
    except ZeroDivisionError:
        return "Nie można dzielić przez zero!"
    except TypeError:
        return "Podaj liczby!"

print(f"10 / 2 = {dziel(10, 2)}")
print(f"10 / 0 = {dziel(10, 0)}")

# ============================================
# 14. ZADANIE DOMOWE
# ============================================

print("\n" + "=" * 50)
print("ZADANIE DOMOWE - DZIEŃ 2")
print("=" * 50)
print("""
1. Stwórz funkcję, która przyjmuje imię i wiek, a zwraca:
   - Ilata w miesiącach
   - Czy osoba jest pełnoletnia
   
2. Stwórz funkcję, która przyjmuje listę liczb i zwraca:
   - Sumę
   - Średnią
   - Największą liczbę
   
3. Stwórz słownik z danymi o sobie (minimum 5 pól)
   
4. Stwórz funkcję, która zamienia temperaturę z °C na °F
   (wzór: °F = °C * 9/5 + 32)
   
5. Użyj list comprehension, aby stworzyć listę kwadratów liczb 0-10
""")

# ============================================
# PRZYKŁADOWE ROZWIĄZANIA DO ZADANIA
# ============================================

print("\n--- PRZYKŁADOWE ROZWIĄZANIA ---")

# Zadanie 1
def analiza_osoby(imie, wiek):
    miesiace = wiek * 12
    pelnoletni = wiek >= 18
    return {
        "imie": imie,
        "wiek_miesiace": miesiace,
        "pelnoletni": pelnoletni
    }

osoba = analiza_osoby("Stefan", 36)
print(f"\nAnaliza osoby: {osoba}")

# Zadanie 2
def statystyki(liczby):
    suma = sum(liczby)
    srednia = suma / len(liczby)
    maks = max(liczby)
    return {"suma": suma, "srednia": srednia, "maks": maks}

liczby = [5, 10, 15, 20, 25]
print(f"\nStatystyki {liczby}: {statystyki(liczby)}")

# Zadanie 3
ja = {
    "imie": "Stefan",
    "wiek": 36,
    "miasto": "Warszawa",
    "zawód": "Data Scientist",
    "hobby": ["programowanie", "AI", "ML"]
}
print(f"\nO mnie: {ja}")

# Zadanie 4
def celsius_na_fahrenheit(c):
    return c * 9/5 + 32

print(f"\n25°C = {celsius_na_fahrenheit(25)}°F")
print(f"0°C = {celsius_na_fahrenheit(0)}°F")

# Zadanie 5
kwadraty_0_10 = [i ** 2 for i in range(11)]
print(f"\nKwadraty 0-10: {kwadraty_0_10}")

# ============================================
# PODSUMOWANIE
# ============================================

print("\n" + "=" * 50)
print("DZIEŃ 2 - ZAKOŃCZONY! 🎉")
print("=" * 50)
print("""
✅ Typy danych
✅ Operatory arytmetyczne
✅ Operatory porównania
✅ Operatory logiczne
✅ Konwersja typów
✅ Operacje na stringach
✅ Operacje na listach
✅ Operacje na słownikach
✅ Krotki
✅ Pętle
✅ Funkcje zaawansowane
✅ List comprehensions
✅ Handlowanie błędami

JUTRO: DZIEŃ 3 - STRUKTURY DANYCH (ZAAWANSOWANE)
""")
