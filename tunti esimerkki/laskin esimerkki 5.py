
#yhteenlasku
def summa(num1, num2):
    print(num1 + num2)

#vähemmys
def vähennys(num1, num2):
    print(num1 - num2)

#kertolasku
def kerto(num1, num2):
    print(num1 * num2)

#jalkolasku
def jakolasku(num1, num2):
    print(num1 / num2)



print("valitse mitä toimintoa haluat käyttää: \nA)=Yhteenlasku"
          "\nB=Vähennyslasku \nC=Kertolasku\nD=Jakolasku\nQ=lopettaa")
while True:
    valinta = input("valintasi (A-D): ").upper()
    if valinta == "":
        print("ohjelma lopetaan")
        break

    a = float(input("anna ensimmäinen luku: "))
    b = float(input("anna toinen luku: "))

    if valinta == "A" or valinta == "a":
        summa(a, b)
    elif valinta == "B" or valinta == "b":
        vähennys(a, b)
    elif valinta == "C" or valinta == "c":
       kerto(a, b)
    elif valinta == "D" or valinta == "d":
        jakolasku(a, b)
    else:
        print("valintasi oli virheellinen")
