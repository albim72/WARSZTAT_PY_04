from xml.etree.ElementTree import Element,SubElement
import xml.etree.ElementTree as ET
from prettyfy import pretty

top = Element('autokomis')

#pierwszy samochód
sam1 = SubElement(top,'samochod')

id = SubElement(sam1,'id')
id.text = 'sam1'

marka = SubElement(sam1,'marka')
marka.text = 'Subaru'

model = SubElement(sam1,'model')
model.text = 'Impreza'

poj = SubElement(sam1,'pojemnosc')
poj.text = '2.0'

rok = SubElement(sam1,'rocznik')
rok.text = '1999'

cena = SubElement(sam1,'cena')
cena.text = '56700'

wyp_dod = SubElement(sam1,'wyposazenie_dod')

kolor = SubElement(wyp_dod,'kolor')
kolor.text = 'czarna perła'

klima = SubElement(wyp_dod,'klimatyzacja')
klima.text = 'RTG6458945'

#pierwszy samochód
sam2 = SubElement(top,'samochod')

id = SubElement(sam2,'id')
id.text = 'sam2'

marka = SubElement(sam2,'marka')
marka.text = 'Subaru'

model = SubElement(sam2,'model')
model.text = 'Outback'

poj = SubElement(sam2,'pojemnosc')
poj.text = '2.8'

rok = SubElement(sam2,'rocznik')
rok.text = '2019'

cena = SubElement(sam2,'cena')
cena.text = '164700'

wyp_dod2 = SubElement(sam2,'wyposazenie_dod')

kolor = SubElement(wyp_dod2,'kolor')
kolor.text = 'czerwony metallic'

pod = SubElement(wyp_dod2,'poduszki')
pod.text = '4'

print(pretty(top))

with open("subaru.xml","w",encoding="utf-8") as f:
    f.write(pretty(top))


