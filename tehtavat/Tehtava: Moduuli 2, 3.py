import math
print("Lasketaan suorakulmion piiri ja pinta_ala!")
kanta = float(input("Anna suorakulman kanta: "))
korkeus = float(input("Anna suorakulman korkeus: "))
piiri = 2*kanta+2*korkeus
pinta_ala = kanta*korkeus
print(f"suorakulmion piiri on: {piiri:0.2f} \nsuorakumion pinta-ala on: {pinta_ala:0.2f}")
print("Tack so mycket!")