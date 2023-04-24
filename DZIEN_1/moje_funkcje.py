# przykład 1
n = 100


def fx(n):
    return n * 7


def policz(a: float, b: float, c: int = 5, y: int = 4) -> int:
    global n
    n = (a + b) * y - c + n + fx(b)
    return n


print(policz(5, 7, 3, 2))
print(type(policz(5, 7, 3, 2)))
print(policz(6.6, 7, 5, 1))
print(type(policz(6.6, 7, 2, 3)))
print(n)

print(policz(3, 7, 2))
print(policz(3, 7, 2, 6))
print(policz(3, 7, y=7.4))

#przykład2

# *nazwa -> lista argumentów, **druganazwa = słownik argumentów
def rank(*lang,nrrank,**inne):
    print(f"ranking języków programowania nr {nrrank}-> miejsce, pierwsze: {lang[0]}, drugie: {lang[1]}, trzecie:"
          f" {lang[2]}, rok {inne}")


rank("Java","Python","C++",nrrank=23,rok=2022,kwartal="I")

# langlist = ["Java","Python","C++","C#","Perl"]
# rank(langlist,nrrank=44)

#przykład3
#funkcja anonimowa lambda, w innych językach =>

print((lambda e,g:2*e+g)(3.5,4.5))
b = lambda u:u+99

print(b(56))

def multi(n):
    return lambda a:a*n

print(multi(6)(11))

liczby = [67,2,-9,68,-23,0,77,9,5,66,101,5,-1,34,78,99,11]

nparz = list(filter(lambda x:x%2==0,liczby))
print(nparz)

def parzyste(x):
    return x%2==0

def filtrowanie(dane,test):
    pp = []
    for element in dane:
        if(test(element)):
            pp.append(element)
    return pp

print(filtrowanie(liczby,parzyste))

cube = list(map(lambda x:x**3,liczby))

print(cube)

speclista = [math.sqrt(x)*(x+7) for x in range(1,10_000_000) if x%2==0]
print(sum(speclista))

specdict = {x:math.sqrt(x)*(x+7) for x in range(1,10_000_000) if x%2==0}
print(sum(specdict))

