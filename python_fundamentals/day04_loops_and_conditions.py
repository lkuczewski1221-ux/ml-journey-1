# ============================================
# DZIEŃ 4 - PĘTLE I WARUNKI
# Python dla AI/ML
# ============================================

print("=== DZIEŃ 4: PĘTLE I WARUNKI ===\n")

# ------------------------------------------
# 1. INSTRUKCJE WARUNKOWE (if, elif, else)
# ------------------------------------------
print("=== 1. WARUNKI (if / elif / else) ===\n")

# Prosty warunek
loss = 0.45
if loss > 0.5:
    print("Loss jest wysoki, model jeszcze się uczy")
else:
    print("Loss jest akceptowalny")

# Kilka warunków - elif
dokladnosc = 0.87

if dokladnosc >= 0.95:
    print("Model jest bardzo dobry!")
elif dokladnosc >= 0.85:
    print("Model jest dobry, można go użyć")
elif dokladnosc >= 0.70:
    print("Model jest przeciętny, warto poprawić")
else:
    print("Model wymaga dużo pracy")

# Przykład ML: early stopping
aktualny_loss = 0.12
poprzedni_loss = 0.11
patiencja = 2
licznik_braku_poprawy = 1

if aktualny_loss >= poprzedni_loss:
    licznik_braku_poprawy += 1
    if licznik_braku_poprawy >= patiencja:
        print("Early stopping! Trening przerwany.")
    else:
        print(f"Brak poprawy ({licznik_braku_poprawy}/{patiencja})")
else:
    licznik_braku_poprawy = 0
    print("Model się poprawia, kontynuujemy trening")

print()

# ------------------------------------------
# ZADANIE 1 - WARUNKI
# ------------------------------------------
print("=== ZADANIE 1: Warunki ===")
print("""
Napisz kod, który:
1. Ma zmienną `epoka` = 15
2. Ma zmienną `max_epok` = 20
3. Ma zmienną `loss` = 0.08
4. Sprawdza:
   - Jeśli loss < 0.1 i epoka < max_epok → wypisz "Trening można zakończyć wcześniej"
   - W przeciwnym razie → wypisz "Kontynuujemy trening"
Twój kod poniżej:
""")

# Twój kod tutaj:

epoka = 15
max_epok = 20
loss = 0.08

# Wpisz swój kod tutaj

print()

# ------------------------------------------
# 2. PĘTLA FOR
# ------------------------------------------
print("=== 2. PĘTLA FOR ===\n")

# Podstawowa pętla po range
print("Epoki od 0 do 4:")
for epoka in range(5):
    print(f"  Epoka {epoka}")

print()

# range z start i step
print("Co druga epoka od 0 do 10:")
for epoka in range(0, 11, 2):
    print(f"  Epoka {epoka}")

print()

# Iteracja po liście
modele = ["Gemma", "Llama", "Mistral", "Qwen"]
print("Dostępne modele:")
for model in modele:
    print(f"  - {model}")

print()

# enumerate - kiedy potrzebujemy indeksu
print("Modele z indeksami:")
for i, model in enumerate(modele):
    print(f"  {i}: {model}")

print()

# Przykład ML: symulacja treningu
print("Symulacja prostego treningu:")
losses = []
for epoka in range(5):
    strata = round(1.0 / (epoka + 1), 4)
    losses.append(strata)
    print(f"Epoka {epoka}: loss = {strata}")

print(f"\nZebrane straty: {losses}")
print()

# ------------------------------------------
# ZADANIE 2 - PĘTLA FOR
# ------------------------------------------
print("=== ZADANIE 2: Pętla for ===")
print("""
Stwórz listę `dokladnosci` z 5 wartościami (np. 0.65, 0.72, 0.81, 0.85, 0.89)
Użyj pętli for, żeby dla każdej wartości wypisać:
"Epoka X: accuracy = Y"
(gdzie X to numer epoki zaczynając od 0)
Twój kod poniżej:
""")

# Twój kod tutaj:

dokladnosci = [0.65, 0.72, 0.81, 0.85, 0.89]

# Wpisz swój kod tutaj

print()

# ------------------------------------------
# 3. PĘTLA WHILE
# ------------------------------------------
print("=== 3. PĘTLA WHILE ===\n")

# Podstawowa pętla while
print("Odejmujemy 0.2 od loss aż zejdzie poniżej 0.3:")
loss = 0.9
krok = 0

while loss > 0.3:
    loss = round(loss - 0.2, 2)
    krok += 1
    print(f"Krok {krok}: loss = {loss}")

print("Osiągnięto cel!\n")

# While z break (bezpieczniejsze w ML)
print("Trening z warunkiem stopu (max 10 epok):")
loss = 0.8
epoka = 0
max_epok = 10

while loss > 0.15:
    epoka += 1
    loss = round(loss * 0.7, 4)  # symulacja spadku
    print(f"Epoka {epoka}: loss = {loss}")
    
    if epoka >= max_epok:
        print("Osiągnięto maksymalną liczbę epok!")
        break

print()

# ------------------------------------------
# ZADANIE 3 - PĘTLA WHILE
# ------------------------------------------
print("=== ZADANIE 3: Pętla while ===")
print("""
Użyj pętli while, żeby symulować trening:
- Start: loss = 0.95
- W każdej iteracji: loss = loss * 0.8 (zaokrąglone do 4 miejsc)
- Drukuj "Epoka X: loss = Y"
- Zatrzymaj pętlę gdy loss < 0.2 LUB gdy epoka >= 8
- Na końcu wypisz ile epok wykonano
Twój kod poniżej:
""")

# Twój kod tutaj:

loss = 0.95
epoka = 0
max_epok = 8

# Wpisz swój kod tutaj

print()

# ------------------------------------------
# ZADANIE 4 - POŁĄCZONE (warunki + pętle)
# ------------------------------------------
print("=== ZADANIE 4: Warunki + Pętle (mały projekt) ===")
print("""
Stwórz prosty symulator treningu:
- Użyj pętli for po range(1, 11)  (10 epok)
- W każdej epoce oblicz "loss" jako 1.0 / epoka (zaokrąglone do 4 miejsc)
- Jeśli loss < 0.15 → wypisz "Wczesne zatrzymanie na epoce X" i przerwij pętlę (użyj break)
- Na końcu wypisz listę wszystkich zebranych strat
Twój kod poniżej:
""")

# Twój kod tutaj:

zebrane_straty = []

# Wpisz swój kod tutaj

print()

# ============================================
# PODSUMOWANIE DNIA 4
# ============================================
print("=" * 50)
print("PODSUMOWANIE DNIA 4")
print("=" * 50)
print("""
Nauczyłeś się:
- Warunków if / elif / else
- Pętli for (z range i enumerate)
- Pętli while + break
- Łączenia warunków z pętlami (bardzo przydatne w treningu!)

Te konstrukcje są podstawą prawie każdego skryptu ML.
""")

print("Super! Dzień 4 zakończony. Jak chcesz kontynuować? 🚀")