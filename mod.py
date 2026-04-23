from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
import logging

# Konfiguracja logowania, żebyś widział, co się dzieje
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def run_server():
    # Tworzymy rejestry (100 rejestrów wypełnionych zerami)
    # Adresy zaczynają się od 0
    store = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(0, [0]*100)
    )
    context = ModbusServerContext(slaves=store, single=True)
    
    # Opcjonalna identyfikacja urządzenia
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'MojaWirtualnaMaszyna'
    identity.ProductCode = 'AI-Pump-01'

    print("Serwer Modbus wystartował na porcie 5020...")
    # Używamy portu 5020 (502 często wymaga uprawnień admina)
    StartTcpServer(context=context, identity=identity, address=("127.0.0.1", 5020))

if __name__ == "__main__":
    run_server()