from osoba import Osoba

print("Obiekty klasy Osoba")
print("*"*36)
os1 = Osoba("Feliks",43,88,178)
print(os1)
os1.print_osoba()
print(f"czy osoba jest Trenerem? -> {os1.czytrener()}")
