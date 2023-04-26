from pojazd import Pojazd

pj = Pojazd()
od = 456
lt = 42
cena_l = 6.51
print(f"spalanie [l/100km]: {pj.spalanie100(od,lt):.2f}")
print(f"koszt przejazdu na trasie {od} km wynosi {pj.kosztyprzejazdu(od,lt,cena_l)} zł")
