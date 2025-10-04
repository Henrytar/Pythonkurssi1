#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#oisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

luvut = int(input("alkuluvun ilmoittaja. Anna luku: "))

if luvut < 2:
    #koska alkuluvut eivät ole alle 2

    print(f"{luvut} ei ole alkuluku.")

    # johtaa siihen, että print
else:
    neliojuuri = int(luvut**0.5)

    #neliöjuuresta saadaan, että luku on jaollinen itsellään

    for x in range(2, neliojuuri + 1):
        if luvut % x == 0:
            print(f"{luvut} ei ole alkuluku.")
            break
    else:
        print(f"{luvut} on alkuluku.")