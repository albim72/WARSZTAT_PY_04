try:
    #x=2
    print(x)
except NameError:
    print("x nie jest zdefiniowany")
except TypeError:
    print("niewłaściwa wartość")
except:
    print("nieoczekiwany błąd!")

#else jest wyłączony z obsługi w momencie wystąpienia wyjątku
else:
    print(f"dwukrotność x = {2*x}")

finally:
    try:
        y = 90
        print(f"y = {y}")
    except NameError:
        print("y nie jest zdefiniowany")
    finally:
        print("wewnetrzne finally...")


print("ciąg dalszy programu")

