print("to pierwsza linia skryptu")

# komentarz jednoliniowy
# CTRL+D -> powieleni linii lub bloku tekstu
#CTRL+/ -> komentowanie/odkomentowanie linii - bloku
"""
komentarz dokumentacyjny
wieloliniowy
"""
'''
drugi wieloliniowy
niedokumentacyjny
'''
imiona = ["Jan","Olga","Karol","Henryk","Nadia","Jan","Danuta"]
print(imiona)
print(type(imiona))
print(imiona[4])
print(imiona[1:5])
print(imiona[-2])
sl = "kalejdoskop"
print(sl)
print(sl[0])
print(sl[2:5])
print(imiona[0][2])
imionaparz = imiona[1::2]
print(imionaparz)
odwr = imiona[3][::-1]
print(odwr)
imiona.append("Jacek")
print(imiona)
imiona.insert(3,"Maria")
print(imiona)
imiona.remove("Danuta")
print(imiona)
del imiona[5]
print(imiona)
print(sorted(imiona))
print(imiona)
imiona.sort()
print(imiona)

#krotka

miasta = ("Kraków","Warszawa","Lublin","Rzeszów","Poznań","Kraków")
print(miasta)
print(miasta[2:4])

#zbiór

kolory = {"zielony","żółty","szary","czarny","biały","czarny","czerwony","czarny"}

print(kolory)
print(kolory)
print(kolory)

kolory.add("fioletowy")

print(kolory)

kolory.update(["niebieski","navy","magenta"])
print(kolory)

liczby = [4,6,8,2,3,1,3,3,4,5,8,11,23,1,3,4,5,2,4,12,3,2,4,5,7,8]


print(liczby)
liczby_zb = set(liczby)
liczby = list(liczby_zb)

print(liczby)

#słownik
osoba = {
    "imię":"Lidia",
    "nazwisko":"Kot",
    "miasto":"Kraków",
    "rok_urodz":1980
}

print(osoba)
print(osoba["miasto"])
osoba["kolor_oczu"] = "brązowe"
print(osoba)

osoba1 = osoba
print(osoba1)


#tworzenie nowej in stancji: dict(),set(),list(),tuple()
osoba2 = dict(osoba)

osoba["nazwisko"] ="Nowikowska"
print(osoba1)

print(osoba2)

print(osoba.keys())
print(osoba.values())
print(osoba.items())

for x,y in osoba.items():
    print(f"{x}: {y}")


