#yhteenlasku

def yhteenlasku(a, b):
    z = a + b
    y = a / b
    return z, y

a = float(input("anna ensimmäinen luku: "))
b =float(input("anna toinen luku: "))

summa, osamaara = yhteenlasku(a, b)

print(f"summa on: ", summa)
print(f"osamäärä on: ", osamaara)