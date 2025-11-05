#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
#Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
#Muunnos on tehtävä aliohjelmaa hyödyntäen.
#Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

def bensiini(syote):
    litrat = 3.785 * syote
    return litrat

yhteensa = []

while True:
    _syote = float(input("Kuinka monta gallonia bensaa löytyy?: "))
    
    if _syote < 0:
        print ("kiitos ja näkemiin")
        break

    ylitrat = bensiini(_syote)
    yhteensa.append((_syote, ylitrat))

    print(f"{_syote:.1f} gallonaa = {ylitrat:.1f} litraa")