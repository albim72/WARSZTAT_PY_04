#przykład1

def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik konkursu {imie}, liczba punktów: {punkty}."

def osoba(funkcja,*args):
    return funkcja(*args)


print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",67))

#przykład2

def rejestracja(oplata):
    def zapisany():
        return "jesteś na liście zawodników"
    def brak():
        return "masz 3 dni aby dokonać wpłaty za zawody..."
    def error():
        return "kod wpłaty błędny: musi być albo 1 - wpłata albo 0 - brak"

    if oplata == 1:
        return zapisany
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(15)())


#przykład3

def startstop(funkcja):
    def wrapper(*args):
        print("uruchomienie programu...")
        funkcja(*args)
        print("zamykanie programu...")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka")

zw = startstop(zawijanie)
zw("czekoladek")

zawijanie("pierników")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} w urodziny...")


dmuchanie("świeczek")

