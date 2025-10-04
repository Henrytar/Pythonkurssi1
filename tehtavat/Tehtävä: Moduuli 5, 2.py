#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.
 
 
numerot = []

while True:
    luku = input("syötä lukuja ja annan lopuksi 5 suurinta järjestyksessä. Tyhjälyönti lopettaa syöttämisen")
    if luku == "":
         break

    numerot.append(float(luku))

numerot.sort(reverse=True)

print(f"viisi suurinta numeroa: {numerot[:5]}")