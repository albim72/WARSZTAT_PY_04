from osoba import Osoba
from klub import Klub
from sport import Sport,Ekstra

class Trener(Osoba,Klub,Sport,Ekstra):
    def __init__(self, imie, wiek, waga, wzrost,
                 nr_licencji,dosw_lata,expert,
                 nr_kb,nazwa_kb,miasto,
                 dyscyplina,lata_upr,wynik):
        Osoba.__init__(self,imie, wiek, waga, wzrost)
        Klub.__init__(self,nr_kb,nazwa_kb,miasto)
        Sport.__init__(self,dyscyplina,lata_upr,wynik)
        self.nr_licencji = nr_licencji
        self.dosw_lata = dosw_lata
        self.expert = expert
        self.trener = True

    def print_trener(self):
        print(f"Trener -> licencja {self.nr_licencji}, lata doświadczenia: {self.dosw_lata}, "
              f"ekspert? {self.expert}")

    def opis(self):
        return "to jest trener!"






