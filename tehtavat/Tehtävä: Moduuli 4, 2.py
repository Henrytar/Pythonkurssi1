print("Tuumat senttimetreiksi")
while True:
    tuumat = float(input("anna pituus tuumina:"))

    if tuumat < 0:
        print("ohjelma lopetetaan!!")
        break

    luku = tuumat * 2.56
    print(f"näin monta senttimetriä: {luku:.2f}")
     

