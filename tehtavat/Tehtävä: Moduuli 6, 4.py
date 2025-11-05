#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def summa(lista):
    tulos = 0
    for luku in lista:
        tulos += luku
    return tulos

luvut = [1, 4, 6, 8, 10]
kokonais_summa = summa(luvut)
print(f"Listan {luvut} summa on {kokonais_summa}.")