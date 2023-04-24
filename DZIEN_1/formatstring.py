marka = "Jeep"
model = "Cherokee"
rocznik = 2019

print(marka,model,rocznik, sep=" --- ",end="////")
print("to jest druga linia")
print("samochód marki " + marka + ", rocznik: " + str(rocznik))

print("samochód marki {}, rocznik: {}.".format(marka,rocznik))

print(f"samochód marki {marka}, rocznik: {rocznik}.")

konkurs = [
    ("Jan",76),
    ("Anna",65),
    ("Olaf",87.5),
    ("Olga",80),
    ("Nadia",55),
    ("Benedykt",23)
]

print("_"*35)

print("________ zestawienie wyników konkursowych ____________")

for i,(imie,punkty) in enumerate(konkurs):
    print('nr %d: %-8s : %.1f punktów' %(i+1,imie,punkty))
