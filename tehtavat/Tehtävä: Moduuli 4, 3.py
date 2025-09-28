print("Syötä lukuja ja annan sulle suurimman/pienemmän luvun :). Tyhjälyönti lopettaa syötön")
luku = []
while True:
    anna = input("anna luku:")
    if anna == "":
        break
    luku.append(float(anna))
print(f"pienin luku {min(luku)} ja suurin luku {max(luku)}")