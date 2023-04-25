from osoba import Osoba
from trener import Trener
from klient import Klient

print("Obiekty klasy Osoba")
print("*"*36)
os1 = Osoba("Feliks",43,88,178)
print(os1)
os1.print_osoba()
print(f"czy osoba jest Trenerem? -> {os1.czytrener()}")
print(os1.opis())

print("Obiekty klasy Trener")
print("*"*36)

tr1 = Trener("Olga",27,52,173,5564,7,True,5,"Samson","Kraków","Trójbój",4,"340kg")
tr1.print_osoba()
tr1.print_trener()
tr1.infoklub()
tr1.infosport()
print(tr1.opis())

print("*"*36)
print("Obiekty klasy Klient")
print("*"*36)

kl1 = Klient("Jan",55,109,174,65455,"roczny",6,"Dragon","Lublin","pływanie",10,"100m - 1min 23s")
kl1.print_osoba()
kl1.infoklub()
kl1.infosport()
print(kl1.opis())
print(f"czy osoba jest Trenerem? -> {os1.czytrener()}")



