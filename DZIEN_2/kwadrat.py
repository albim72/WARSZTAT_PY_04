class Basic:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def wynik(self):
        return self.a*(self.b/2)
    
class Second:
    def __new__(cls,a,b):
        if a > b:
            return Basic(a,b)
        return object.__new__(Second)
    
    def __init__(self,a,b):
        self.a = a+100;
        self.b = b+200;
        
    def wynik(self):
        return self.a - (self.b/2)
