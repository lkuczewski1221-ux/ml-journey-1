import torch
import torch.nn as nn
import torch.optim as optim

print("--- BUDOWA SIECI NEURONOWEJ ---")

# 1. Definiujemy sprzęt (Akceleracja M5 Pro)
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"Używamy procesora AI: {device}")

# 2. Dane treningowe: Logika XOR
# Wejścia (X) - 4 kombinacje zera i jedynki
X = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]], device=device)
# Oczekiwane wyjścia (Y)
Y = torch.tensor([[0.0], [1.0], [1.0], [0.0]], device=device)

# 3. Architektura Sieci
class SiecXOR(nn.Module):
    def __init__(self):
        super(SiecXOR, self).__init__()
        # Warstwa ukryta: z 2 wejść robimy 8 neurony
        self.warstwa1 = nn.Linear(2, 8) 
        self.aktywacja1 = nn.ReLU() # Wprowadza nieliniowość
        
        # Warstwa wyjściowa: z 8 neuronów robimy 1 wynik
        self.warstwa2 = nn.Linear(8, 1) 
        self.aktywacja2 = nn.Sigmoid() # Zwraca wynik od 0 do 1 (prawdopodobieństwo)

    def forward(self, x):
        # Przepływ danych przez sieć
        x = self.warstwa1(x)
        x = self.aktywacja1(x)
        x = self.warstwa2(x)
        x = self.aktywacja2(x)
        return x

model = SiecXOR().to(device)

# 4. Funkcja błędu i Nauczyciel (Optymalizator)
kryterium = nn.BCELoss() # Binary Cross Entropy - idealna do zadań Tak/Nie
optymalizator = optim.SGD(model.parameters(), lr=0.1) # Stochastic Gradient Descent

# 5. Proces Treningu
epoki = 50000
print("\nRozpoczynam trening (uczenie się na błędach)...")

for epoka in range(epoki):
    # Krok A: Zgaduj wyniki
    przewidywania = model(X)
    
    # Krok B: Policz, jak bardzo się pomyliłeś
    blad = kryterium(przewidywania, Y)
    
    # Krok C: Wyciągnij wnioski i popraw wagi
    optymalizator.zero_grad() # Czyścimy pamięć
    blad.backward()           # Obliczamy, co poszło nie tak (Propagacja wsteczna)
    optymalizator.step()      # Aktualizujemy połączenia w mózgu sieci

    # Pokazuj postępy co 1000 epok
    if (epoka + 1) % 1000 == 0:
        print(f"Epoka: {epoka+1}/{epoki} | Błąd (Loss): {blad.item():.4f}")

# 6. Egzamin końcowy (Test)
print("\n--- EGZAMIN KOŃCOWY ---")
with torch.no_grad(): # Wyłączamy tryb uczenia, tylko testujemy
    wyniki = model(X)
    for i in range(len(X)):
        dane_wejsciowe = X[i].cpu().numpy()
        odpowiedz_sieci = wyniki[i].item()
        werdykt = round(odpowiedz_sieci)
        print(f"Pytanie {dane_wejsciowe} -> Odpowiedź sieci: {odpowiedz_sieci:.4f} (Zaokrąglając: {werdykt})")