from pymodbus.client import ModbusTcpClient
import time

# Konfiguracja połączenia
# 'localhost' oznacza, że symulator działa na Twoim komputerze
SERVER_IP = '127.0.0.1' 
PORT = 502

def monitor_machine():
    # Inicjalizacja klienta
    client = ModbusTcpClient(SERVER_IP, port=PORT)
    
    print(f"--- Próba połączenia z maszyną na {SERVER_IP}:{PORT} ---")
    
    if client.connect():
        try:
            while True:
                # Odczytujemy 1 rejestr typu 'Holding Register' z adresu 1
                # W automatyce to może być np. temperatura silnika
                result = client.read_holding_registers(address=1, count=1)
                
                if not result.isError():
                    raw_value = result.registers[0]
                    # Skalowanie: np. czujnik wysyła 255 dla 25.5 stopnia
                    temperature = raw_value / 10.0
                    
                    print(f"Aktualna temperatura: {temperature}°C")
                    
                    # Logika "Pre-AI": zwykły próg (if-else)
                    # W przyszłości tu wejdzie Twój model ML
                    if temperature > 50.0:
                        print("!!! ALARM: Przegrzanie silnika !!!")
                else:
                    print("Błąd odczytu danych z rejestru.")
                
                time.sleep(2) # Czekaj 2 sekundy przed kolejnym odczytem
                
        except KeyboardInterrupt:
            print("\nZatrzymano monitorowanie.")
        finally:
            client.close()
            print("Połączenie zamknięte.")
    else:
        print("Błąd: Nie można połączyć się z symulatorem Modbus. Czy Ananas/ModbusPal jest włączony?")

if __name__ == "__main__":
    monitor_machine()