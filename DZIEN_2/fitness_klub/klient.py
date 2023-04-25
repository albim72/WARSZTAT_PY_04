from trener import Trener

class Klient(Trener):
    def __init__(self, imie, wiek, waga, wzrost,
                 id_klienta,rodzaj_karnetu,
                 nr_kb, nazwa_kb, miasto, dyscyplina,
                 lata_upr, wynik,
                 nr_licencji="", dosw_lata="", expert=""):
        super().__init__(imie, wiek, waga, wzrost, nr_licencji, dosw_lata, expert, nr_kb, nazwa_kb, miasto, dyscyplina,
                         lata_upr, wynik)
        self.id_klienta = id_klienta
        self.rodzaj_karnetu = rodzaj_karnetu
        print(self.przydzial_nr())
        if self.nr_licencji != "":
            self.trener = True
        else:
            self.trener = False

    def przydzial_nr(self):
        return f"przydzielono numer klienta: {self.id_klienta}."

    def opis(self):
        return "to jest klient!"



