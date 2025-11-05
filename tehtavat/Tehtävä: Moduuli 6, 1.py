#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
#Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
#Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def nopanheitto():
    x = random.randint(1, 6)
    return x
luku = 0
while luku != 6:
    luku = nopanheitto()
    print(f"heiton tulos: {luku}")