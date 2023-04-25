class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.trener = False
        print("utworzono nowy obiekt klasy osoba...")

    #funkcja konstrukcyjna (specjalna) która tworzy reprezentację tekstową obiektu i zasłania
    #podstawową definicję obiektu
    def __repr__(self):
        return f"Nowa osoba -> kolor oczu: {self.kolor_oczu}"

    def print_osoba(self):
        print(f"osoba -> {self.imie}, wiek: {self.wiek} lat, waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm")

    def czytrener(self):
        return self.trener

    def opis(self):
        return "To jest podstawowa osoba"








