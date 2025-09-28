oikeatunnus = "puthon"
oikeasalasana = "rules"

maksimi = 5
yritys = 0

while yritys < maksimi:
    tunnus= input("syötä käyttäjätunnus: ")
    salasana= input("syötä salasana: ")


    if tunnus == oikeatunnus and salasana == oikeasalasana:
        print("tervetuloa!")
        break
    else:
        yritys += 1
else:
    print("Kokeile myöhemmin uudelleen!")
