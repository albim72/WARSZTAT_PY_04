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


#przykład2

# *nazwa -> lista argumentów, **druganazwa = słownik argumentów
def rank(*lang,nrrank,**inne):
    print(f"ranking języków programowania nr {nrrank}-> miejsce, pierwsze: {lang[0]}, drugie: {lang[1]}, trzecie:"
          f" {lang[2]}, rok {inne}")


rank("Java","Python","C++",nrrank=23,rok=2022,kwartal="I")


