import torch

print("--- TEST ŚRODOWISKA AI ---")
print(f"Wersja PyTorch: {torch.__version__}")

# Sprawdzamy, czy PyTorch widzi Apple Silicon GPU (MPS)
if torch.backends.mps.is_available():
    mps_device = torch.device("mps")
    print("✅ SUKCES: M5 Pro GPU (MPS) jest widoczne i gotowe do akcji!")
    
    # Tworzymy prosty tensor (macierz) bezpośrednio w pamięci układu graficznego
    x = torch.ones(5, device=mps_device)
    print(f"Wygenerowany tensor na GPU: \n{x}")
else:
    print("❌ BŁĄD: System nie widzi GPU. Policzmy to na zwykłym procesorze.")