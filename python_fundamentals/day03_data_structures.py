# ==========================================
# DZIEŃ 3: STRUKTURY DANYCH
# ==========================================
# Czas poznać sposoby na przechowywanie wielu danych w jednej zmiennej!
# W Machine Learningu będziemy ciągle operować na ogromnych zbiorach,
# więc to absolutna podstawa.

# ------------------------------------------
# 1. LISTY (Lists) - Zmienne i uporządkowane
# ------------------------------------------
print("=== 1. LISTY ===")
modele_ai = ["Gemma", "Llama", "GPT-4", "Claude"]
print(f"Moja lista modeli: {modele_ai}")

# Dostęp do elementów (indeksowanie zaczyna się od 0!)
print(f"Pierwszy model: {modele_ai[0]}")
print(f"Ostatni model: {modele_ai[-1]}") # -1 oznacza ostatni element

# Modyfikacja listy
modele_ai.append("Mistral") # Dodaje na koniec
modele_ai[1] = "Llama-3"    # Zamienia element
print(f"Zaktualizowana lista: {modele_ai}")

# ==========================================
# ZADANIE 1: 
# Stwórz listę `epoki_treningowe` z 5 dowolnymi liczbami (np. 10, 20, 30...)
# i wydrukuj jej drugi element oraz długość listy (użyj funkcji len()).
# Twój kod poniżej:

# Rozwiązanie Zadania 1
epoki_treningowe = [10, 20, 30, 50, 100]          # 5 przykładowych wartości epok

print(f"Drugi element listy: {epoki_treningowe[1]}")   # indeks 1 = drugi element (Python liczy od 0)
print(f"Długość listy: {len(epoki_treningowe)}")

# ------------------------------------------
# 2. KROTKI (Tuples) - Niezmienne (immutable)
# ------------------------------------------
print("\n=== 2. KROTKI ===")
# Krotki są jak listy, ale nie można ich modyfikować. Są szybsze i bezpieczniejsze
# dla danych, które nie powinny się zmienić (np. wymiary obrazka).
wymiary_obrazu = (1920, 1080, 3) # Szerokość, wysokość, kanały RGB
print(f"Wymiary obrazu do analizy: {wymiary_obrazu}")

# ==========================================
# ZADANIE 2:
# Stwórz krotkę `wspolrzedne_gps` zawierającą dwie liczby zmiennoprzecinkowe
# (szerokość i długość geograficzną) i wydrukuj ją. Zobaczysz, że nie możesz
# użyć `.append()` na krotce.
# Twój kod poniżej:

# Rozwiązanie Zadania 2
wspolrzedne_gps = (52.2297, 21.0122)  # przykład: Warszawa (szerokość, długość)

print(f"Współrzędne GPS: {wspolrzedne_gps}")

# Demonstracja, że krotki są niemodyfikowalne
try:
    wspolrzedne_gps.append(0.0)
except AttributeError:
    print("Błąd: Nie można wywołać .append() na krotce (tuple jest immutable)")

# ------------------------------------------
# 3. SŁOWNIKI (Dictionaries) - Klucz-Wartość
# ------------------------------------------
print("\n=== 3. SŁOWNIKI ===")
# Słowniki są idealne do przechowywania parametrów i konfiguracji w AI.
hiperparametry = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "optimizer": "Adam"
}
print(f"Konfiguracja modelu: {hiperparametry}")

# Dostęp i modyfikacja po kluczu
print(f"Rozmiar batcha wynosi: {hiperparametry['batch_size']}")
hiperparametry["epochs"] = 100 # Dodanie nowego klucza
print(f"Słownik po dodaniu epok: {hiperparametry}")

# ==========================================
# ZADANIE 3:
# Stwórz słownik `moj_komputer`, który będzie zawierał informacje:
# 'procesor': "M5", 'ram_gb': 24, 'czy_gpu_wlaczone': True
# Wydrukuj wartość klucza 'ram_gb'.
# Twój kod poniżej:

# Rozwiązanie Zadania 3
moj_komputer = {
    'procesor': "M5",
    'ram_gb': 24,
    'czy_gpu_wlaczone': True
}

print(f"Rozmiar RAM w Twoim komputerze: {moj_komputer['ram_gb']} GB")

# ------------------------------------------
# 4. ZBIORY (Sets) - Unikalne elementy
# ------------------------------------------
print("\n=== 4. ZBIORY ===")
# Zbiory same usuwają duplikaty i nie mają kolejności.
tagi_zdjec = {"pies", "kot", "pies", "samochód", "kot"}
print(f"Unikalne tagi: {tagi_zdjec}") # 'pies' i 'kot' pojawią się tylko raz!

# ==========================================
# ZADANIE 4:
# Masz dwie listy słów z dwóch różnych tekstów. Użyj zbiorów (set()), aby 
# znaleźć tylko te unikalne słowa dla obu z nich łącznie. 
# Zmień obie listy na set(), i spróbuj użyć operatora `|` (suma zbiorów)
# żeby połączyć te dwa zbiory i przypisać wynik do zmiennej.
tekst_1 = ["AI", "to", "przyszłość"]
tekst_2 = ["AI", "uczy", "się"]
# Twój kod poniżej:

# Rozwiązanie Zadania 4
set1 = set(tekst_1)
set2 = set(tekst_2)
unikalne_slowa = set1 | set2   # | oznacza sumę zbiorów (union)

print(f"Unikalne słowa z obu tekstów: {unikalne_slowa}")

print("\nSuper! Jak uzupełnisz kod, po prostu uruchom go lub wklej mi rozwiązanie, a omówimy wyniki! 🚀")
