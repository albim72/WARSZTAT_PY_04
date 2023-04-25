import math


def policz(a,b):
    try:
        x = math.sqrt(a / b)

    except ValueError as ve:
        print(ve)
        print("pierwiastek z liczby ujemnej!")
    except ZeroDivisionError as ze:
        print(ze)
        print("dzielenie przez 0")
    else:
        print(f"wartość x wynosi {x}")
    finally:
        print("policzmy coś jeszcze")

try:
    a = int(input("podaj wartość a: "))
    b = int(input("podaj wartość b: "))
    if b!=0:
        if (a*b>=0):
            policz(a,b)
        else:
            print("iloraz a/b nie może być ujemny")
    else:
        print("b nie może być ujemne")

except ValueError:
    print("brak danych, albo zły format!")

