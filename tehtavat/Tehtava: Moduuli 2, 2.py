import math
sade = float(input("Anna ympyrän säde:"))
#float mahdollistaa tekstin muutua numeroiksi
pinta_ala = (2*sade*math.pi)
# käyttämällä "f" mahdollistaa sen, että "string" voidaan upottaa laskutoimituksia ilman "+" merkkejä.
print(f"Ympyrän pinta-ala on: {pinta_ala:0.2f}")
