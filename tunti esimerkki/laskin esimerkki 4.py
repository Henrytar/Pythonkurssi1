print("valitse mitä toimintoa haluat käyttää: \nA)=Yhteenlasku"
      "\nB=Vähennyslasku \nC=Kertolasku\nD=Jakolasku")
valinta = input("valintasi (A-D): ").upper()

if valinta == "A" or valinta == "a":
    a = float(input("anna ensimmäinen luku: "))
    b = float(input("anna toinen luku: "))
    print("yhteenlasku", a+b)
elif valinta == "B" or valinta == "b":
    a = float(input("anna ensimmäinen luku: "))
    b = float(input("anna toinen luku: "))
    print("vähennyslasku", a-b)
elif valinta == "C" or valinta == "c":
    a = float(input("anna ensimmäinen luku: "))
    b = float(input("anna toinen luku: "))
    print("kertolasku", a*b)
elif valinta == "D" or valinta == "d":
    a = float(input("anna ensimmäinen luku: "))
    b = float(input("anna toinen luku: "))
    print("jakolasku", a/b)
else:
    print("valintasi oli virheellinen")
