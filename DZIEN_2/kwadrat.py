class Basic:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def wynik(self):
        return self.a*(self.b/2)

class Empty:
    def __init__(self,a,b):
        self.a = a+10;
        self.b = b+20;
    def wynik(self):
        return self.a + self.b
class Second:
    def __new__(cls,a,b):
        if a > b:
            return Basic(a,b)
        elif a == 10:
            return Empty(a,b)
        return object.__new__(Second)

    def __init__(self,a,b):
        self.a = a+100;
        self.b = b+200;

    def wynik(self):
        return self.a - (self.b/2)


b1 = Second(45,5)
b2 = Second(45,55)
b3 = Second(10,10)

print(f"wynik dla {b1.__class__.__name__} wynosi {b1.wynik()}")
print(f"wynik dla {b2.__class__.__name__} wynosi {b2.wynik()}")
print(f"wynik dla {b3.__class__.__name__} wynosi {b3.wynik()}")
