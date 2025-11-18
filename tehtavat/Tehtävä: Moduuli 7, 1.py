#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
#Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
#Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.


tulos = int(input("anna kuukausi numerona (1-12), niin kerron mikä vuodenaika on.. yo yo: "))
kuukaudet = ("Talvi","Talvi",
             "Kevät","Kevät","Kevät",
             "Kesä","Kesä","Kesä",
             "syksy","syksy","syksy",
             "Talvi",)

if 1 <= tulos <= 12:
    lopputulos = kuukaudet[tulos-1]
    print(lopputulos)
else:
    print("Yo yo, maassa on 12kk, joten 1-12 väliltä, kiitos!")