import random

def nopanheitto(pienin, suurin):
    x = random.randint(pienin, suurin)
    return x

pienin = int(input("kerro pienin nopan luku: "))
suurin= int(input("kerro suurin nopan luku: "))

luku = 0

while luku != suurin:
    luku = nopanheitto(pienin, suurin)
    print(f"heiton tulos: {luku}")