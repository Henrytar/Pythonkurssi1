#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.

import random
arpa = int(input("Anna arpakuutioiden määrän ja heitän kaikkia noppia samaan aikaan + lasken yhteen!!!"))
summa = 0

for muututuja in range(arpa):

    silmaluku = random.randint(1, 6)
    summa += silmaluku

print(f"silmalukujen yhteismäärä:{summa}")