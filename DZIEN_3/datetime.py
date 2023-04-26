import datetime
from datetime import time as tm,date
import time
from timeit import default_timer as timer


dt_object = datetime.datetime.now()
print(dt_object)

date_object = date.today()
print(date_object)

print(dir(datetime))

print(f"minimalny rok daty:{datetime.MINYEAR}")
print(f"maksymalny rok daty:{datetime.MAXYEAR}")

print(f"zadeklarowana data: {datetime.date(1964,8,3)}")
print(f"dolna granica daty: {date.min}")
print(f"górna granica daty: {date.max}")

print(f"data liczona od Epoki w [s]: {date.fromtimestamp(1)}")

obj = time.gmtime(0)
print(obj)
epoka = time.asctime(obj)
print(epoka)

timesec = time.time()
print(timesec)

a = tm(11,53,34,2)
print(f"godzina: {a.hour}")
print(f"minuty: {a.minute}")
print(f"sekundy: {a.second}")
print(f"mikrosekundy: {a.microsecond}")


def oblicz(num):
    return sum([i**8 for i in range(num)])

start=time.time()
wynik = oblicz(10_000_000)
end = time.time()

print(f"wynik: {wynik}, czas wykonania: {end-start} s")

start2 = timer()
wynik = oblicz(10_000_000)
end2 = timer()
print(f"drugi wynik: {wynik}, czas wykonania: {end2-start2} s")



