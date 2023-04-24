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
