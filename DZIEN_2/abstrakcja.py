from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x

    def msg(self,info):
        return f"ważna informacja: {info}"

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*4

class Regular(Prototyp):

    def __init__(self, x, y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return 1001

    def policz_x(self):
        return super().policz_x() + 7*self.y


r = Regular(4,7)
print(f"wynik policz -> {r.policz()}")
print(f"wynik policz_x -> {r.policz_x()}")
print(r.msg("to jest dodatkowa opcja"))

