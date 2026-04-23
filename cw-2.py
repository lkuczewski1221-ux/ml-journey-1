print("==ZMIENNE==")

liczba_calkowita = 44
print(f"int: {liczba_calkowita} - typ: {type(liczba_calkowita)}")

liczba_dziesietna = 3.66
print(f"float: {liczba_dziesietna} - typ: {type(liczba_dziesietna)}")

tekst = "Python AI/ML"
print(f"str: '{tekst}' - typ: {type(tekst)}")

prawda = True
falsz = False

print(f"bool: {prawda} - typ: {type(prawda)}")
print(f"bool: {falsz} - typ: {type(falsz)}")

nic = None

print(f"NoneType: {nic} - typ: {type(nic)}")

model_ai = "SuperGemma26b Heretic"
wersja = 0.6
czy_dziala = True

print(f"str: '{model_ai}' - typ {type(model_ai)}"  f"\nfloat: {wersja} - typ: {type(wersja)}" f"\nbool: {czy_dziala} - typ: {type(czy_dziala)}")

#===Operatory Arytmetyczne===

print("=" * 25 )
print("Operatory Arytmetyczne")
print("=" * 25 )

zdjecia_razem = 1000
max_analiza = 32

print(f"{zdjecia_razem // max_analiza}")
print(f"{zdjecia_razem % max_analiza}")

#===Operatory Logiczne===

print("=" * 25)
print("Operatory Logiczne")
print("=" * 25)


obecny_blad = 0.45
max_blad = 0.1
epoki = 50
max_epok = 50

czy_trenowac_dalej = (obecny_blad >= max_blad) and (epoki < max_epok)
print(f"Czy trenowac dalej? {czy_trenowac_dalej}")

#===Tekst Funkcje===

print("=" * 25)
print("Tekst Funkcje")
print("=" * 25)

tekst = "Apple M5 Pro 24GB RAM jest super do kodowania"

print (tekst)
print (tekst.upper())
print (tekst.lower())
print (tekst.replace("24", "128"))
