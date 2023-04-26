class Samochod:
    def __init__(self,marka,model,rocznik,cena,rata):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.cena = cena
        self.rata = rata

    @staticmethod
    def salon(miasto):
        return f"salon sprzedaży -> miasto: {miasto}"

    def info(self):
        return "to jest metoda niestatyczna"

    @classmethod
    def obliczenie_raty(cls,cena,miesiac):
        return cls("Opel","Insignia",2019,56000,1.3*cena/miesiac)


sm1 = Samochod("Jeep","Cherokee",2020,202400,3240)
sm2 = Samochod.obliczenie_raty(89700,56)

print(sm1)
print(sm2)

print(f"rata dla samochodu sm1: {sm1.rata:.2f} zł")
print(f"rata dla samochodu sm2: {sm2.rata:.2f} zł")

print(sm1.salon("Toruń"))
print(Samochod.salon("Gdziekolwiek"))

print(sm1.info())
#print(Samochod.info())
