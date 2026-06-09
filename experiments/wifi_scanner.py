import subprocess

def scan_macos_wifi():
    # Ścieżka do narzędzia 'airport' w macOS
    cmd = ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-s"]
    
    try:
        # Uruchomienie komendy i przechwycenie wyniku
        result = subprocess.check_output(cmd).decode('utf-8')
        print("--- Znalezione sieci WiFi ---")
        print(result)
    except Exception as e:
        print(f"Błąd skanowania: {e}")

if __name__ == "__main__":
    scan_macos_wifi()
