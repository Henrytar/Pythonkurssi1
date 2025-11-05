import random

def nopanheitto(pienin, suurin):
    x = random.randint(pienin, suurin)
    return x

_pienin = int(input("kerro pienin nopan luku: "))
_suurin= int(input("kerro suurin nopan luku: "))

luku = 0

while luku != _suurin:
    luku = nopanheitto(_pienin, _suurin)
    print(f"heiton tulos: {luku}")