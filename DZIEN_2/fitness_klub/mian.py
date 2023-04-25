from osoba import Osoba
from trener import Trener
from klient import Klient


mojeob = []
print("Obiekty klasy Osoba")
print("*"*36)
os1 = Osoba("Feliks",43,88,178)
mojeob.append(os1)
print(os1)
os1.print_osoba()
print(f"czy osoba jest Trenerem? -> {os1.czytrener()}")
print(os1.opis())
print(f"wartość BMI: {os1.bmi():.2f}, opis: {os1.opis_bmi()}")

print("Obiekty klasy Trener")
print("*"*36)

tr1 = Trener("Olga",27,52,173,5564,7,True,5,"Samson","Kraków","Trójbój",4,"340kg")
mojeob.append(tr1)
tr1.print_osoba()
tr1.print_trener()
tr1.infoklub()
tr1.infosport()
print(tr1.opis())
print(f"wartość BMI: {tr1.bmi():.2f}, opis: {tr1.opis_bmi()}")

print("*"*36)
print("Obiekty klasy Klient")
print("*"*36)

kl1 = Klient("Jan",55,109,174,65455,"roczny",6,"Dragon","Lublin","pływanie",10,"100m - 1min 23s")
mojeob.append(kl1)
kl1.print_osoba()
kl1.infoklub()
kl1.infosport()
print(kl1.opis())
print(f"czy osoba jest Trenerem? -> {kl1.czytrener()}")
print(f"wartość BMI: {kl1.bmi():.2f}, opis: {kl1.opis_bmi()}")
print("*"*36)
kl2 = Klient("Anna",36,60,176,8765,"otwarty",4,"Fly","Rzeszów","biegi ultra",12,"70km 9h 23min 4s",65446,10,True)
mojeob.append(kl2)
kl2.print_osoba()
kl2.infoklub()
kl2.infosport()
print(kl2.opis())
print(f"czy osoba jest Trenerem? -> {kl2.czytrener()}")
kl2.print_trener()
print(f"wartość BMI: {kl2.bmi():.2f}, opis: {kl2.opis_bmi()}")

print(mojeob)
print(mojeob[0].opis_bmi())

print("_________ opis z iteracji __________")
for i,j in enumerate(mojeob):
    print(mojeob[i].opis_bmi())






