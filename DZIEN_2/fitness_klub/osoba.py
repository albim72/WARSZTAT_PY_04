class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.trener = False
        print("utworzono nowy obiekt klasy osoba...")
        
    def print_osoba(self):
        print(f"osoba -> {self.imie}, wiek: {self.wiek} lat, waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm.")
        
    def czytrener(self):
        return self.trener
