class Sport:
    def __init__(self,dyscyplina,lata_upr,wynik):
        self.dyscyplina = dyscyplina
        self.lata_upr = lata_upr
        self.wynik = wynik
        print(self.sport_przypisanie())
        
    def sport_przypisanie(self):
        return f"dysycyplina: {self.dyscyplina}"
        
    def infosport(self):
        print(f"{self.dyscyplina}, czs uprawiania [lata]: {self.lata_upr}, "
              f"życiówka: {self.wynik}.")
