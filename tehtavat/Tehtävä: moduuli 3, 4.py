#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

print("lasketaanko onko antamasi vuosi karkausvuosi!")
vuosi = int(input("Syötä vuosiluku:"))
if vuosi % 4 == 0 and vuosi % 100 !=0 or vuosi % 400 == 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")
