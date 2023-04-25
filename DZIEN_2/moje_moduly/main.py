#import dane
#import dane as dn
from dane import nr_filii as filia
from dane import book as bk
from funkcje.bfunkcje import czytaj_liste,czytaj_slownik
from klasy.klasadane import CDane

print("wywołanie bespośrednie")
print("*"*36)
print(filia)
print(bk)

print("*"*36)

print("wywołanie przez funkcję...")
print("*"*36)

czytaj_liste(filia)
print("_"*36)
czytaj_slownik(bk)

print("*"*36)

print("wywołanie przez obiekt klasy...")
print("*"*36)

cd = CDane(filia,bk)
cd.czytaj_l()
print("_"*36)
cd.czytaj_s()
