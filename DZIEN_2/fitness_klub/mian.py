from osoba import Osoba
from trener import Trener

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

