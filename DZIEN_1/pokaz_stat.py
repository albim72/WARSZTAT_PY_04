liczby = [56,1009,-1089,0,999,23,45,177,-567,345,667,99,101,34,153,-321,879]
pusta = []

def pokaz_statystyki(lista):
    if len(lista)>0:
        minimum = min(lista)
        maksimum = max(lista)
        roztep = maksimum-minimum
        suma = sum(lista)
        lelem = len(lista)
        sr_art = suma/lelem
        return minimum,maksimum,roztep,lelem,sr_art
    else:
        return "brak danych"


wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maksi,roz,le,sa = pokaz_statystyki(liczby)
print(f"wartość największa: {maksi}, wartość najmniejsza: {mini}, rozstęp: {roz}, liczba elementów: {le}, "
      f"średnia arytmetyczna: {sa}")

print(pokaz_statystyki(pusta))
