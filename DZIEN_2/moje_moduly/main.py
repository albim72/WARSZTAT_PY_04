#import dane
#import dane as dn
from dane import nr_filii as filia
from dane import book as bk
from funkcje.bfunkcje import czytaj_liste,czytaj_slownik

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
