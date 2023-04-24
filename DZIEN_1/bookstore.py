class Book:
    #deklaracja stanu(dane) -> konstruktor klasy
    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(cls, *args, **kwargs)
    def __init__(self,id,tytul,autor,cena=10):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    #definicja zachowania -> funkcje klasy -> metody
    def create_book(self):
        print("utworzono nową książkę!")

    def printbook(self):
        return f"książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self.oprawa}"

    def rabat(self,procent):
        return round(self.cena*(procent/100),2)

    def setcena(self,nowacena):
        self.cena = nowacena

bk = Book(3,"Wiedźmin","Andrzej Sapkowski")
print(bk)
print(bk.printbook())
print(f"rabat od ceny: {bk.rabat(12)} zł")

bk.cena = 44
print("********************************")
print(bk.printbook())
print(f"rabat od ceny: {bk.rabat(12)} zł")

bk.setcena(41)
print("********************************")
print(bk.printbook())
print(f"rabat od ceny: {bk.rabat(12)} zł")


bk2 = Book(78,"Hobbit","J.R.R Tolkien",47)
print("********************************")
bk.setcena(41)
print(bk2.printbook())
print(f"rabat od ceny: {bk2.rabat(12)} zł")
