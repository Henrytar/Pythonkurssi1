import math
print("Hei taas! Tässä joudut antamaan keskiaikaisia mittoja,\njoita en kumminkaan tiedä (jos tiedät hyvä niin!),\njoten anna vain numeroita.")
leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))


luodit = (naula*32+leiviska*20*32+luoti)
gramma = (13.3*luodit)
kilogramma = int(gramma/1000)


print(f"kokonaismassa nykymittojen mukaan {kilogramma}kg ja {gramma-kilogramma*1000:0.2f} grammaa.")



