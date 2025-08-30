import math
print("Lasketaan kolmen KOKONAISLUVUN summan, tulon ja keskiarvon!!")
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

print("Lukujen summa:", summa)
print("Lukujen tulo:", tulo)
print("Lukujen keskiarvo:", keskiarvo)
#tai (harjoitus)
print(f"Lukujen summa: {summa} \nlukujen tulo: {tulo} \nlukujen keskiarvo: {keskiarvo}")