# przykład 1
n=100

def fx(n):
    return n*7

def policz(a: float, b: float, c:  int= 5, y:int=4) -> int:
    global n
    n = (a + b) * y - c + n + fx(b)
    return n

print(policz(5, 7, 3, 2))
print(type(policz(5, 7, 3, 2)))
print(policz(6.6, 7, 5, 1))
print(type(policz(6.6, 7, 2, 3)))
print(n)

print(policz(3,7,2))
print(policz(3,7,2,6))
print(policz(3,7,y=7.4))





