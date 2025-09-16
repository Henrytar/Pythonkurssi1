pituus = int(input("kuinka pitkä olet?"))


if 170 < pituus <= 180:
    print("olepta pitkä! ")

if pituus == 178:
    print("olet yhtä pitkä kuin minä! ")

#tämä muuttaa kaikki lowercase ja ohjelma osaa lukea paremmin!!!
koira = input("mikä on koiran nimi?:").lower()
if koira == "timo":
    print("hieno nimi!!")