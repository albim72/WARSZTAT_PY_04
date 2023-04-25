def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f"element {i+1} o wartości -> (nr filii księgarni) -> {j}")
        
def czytaj_slownik(slownik):
    for x,y in slownik.items():
        print(f"książka: klucz->{x}, wartość: {y}")
