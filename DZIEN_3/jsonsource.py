import json

osobajson = '{"name":"Jan","lastname":"Kot","age":34,"city":"Kraków"}'
print(osobajson)
print(type(osobajson))

osoba = json.loads(osobajson)
print(osoba)
print(type(osoba))

print(osoba["lastname"])

auto = {
    "marka":"Jeep",
    "model":"Cherokee",
    "rocznik":2018,
    "poj":4.4
}

jsonauto = json.dumps(auto,indent=5)
print(jsonauto)

with open("samochod.json","w",encoding="utf-8") as f:
    f.write(jsonauto)

with open("samochod.json","r",encoding="utf-8") as f:
    autodict = json.load(f)

print(autodict)


print("______________________")

with open("pracownik.json","r",encoding="utf-8") as f:
    prac = json.load(f)

print(prac)

print(prac["pra_info"][0]["email"])

print('Klub sportowy: "FC Barcelona"')
