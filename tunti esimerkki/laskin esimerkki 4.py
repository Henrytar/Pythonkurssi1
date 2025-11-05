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
        print("yhteenlasku", a+b)
    elif valinta == "B" or valinta == "b":
        print("vähennyslasku", a-b)
    elif valinta == "C" or valinta == "c":
        print("kertolasku", a*b)
    elif valinta == "D" or valinta == "d":
        print("jakolasku", a/b)
    else:
        print("valintasi oli virheellinen")
