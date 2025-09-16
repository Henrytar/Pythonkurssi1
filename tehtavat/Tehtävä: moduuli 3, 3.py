sukupuoli = input("mikä on biologinen sukupuolesi: ").lower()
hemo = int(input("Mikä on hemolgobiiniarvosi(g/l)?: ").lower())
if sukupuoli == "nainen" :
    if hemo < 117:
        print("hemoglobiini on alhainen")
    elif hemo > 175:
        print("hemoglobiini on korkea")
    else:
        print("hemoglobiini on normaali")
elif sukupuoli == "mies" :
    if hemo < 134:
        print("hemoglobiini on alhainen")
    elif hemo > 195:
        print("hemoglobiini on korkea")
    else:
        print("hemoglobiini on normaali")
else:
    print("valitse (mies/nainen) ja kirjoita hemoglobiiniarvo numeroilla.")
