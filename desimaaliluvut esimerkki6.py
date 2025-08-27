pituus = float(input("anna pituutesi: "))
paino = float(input("anna painosi: "))

bmi = paino /(pituus/100)**2

print("pituus-paino-indeksi on: ", bmi)
print(f"pituus-paino-indeksi on {bmi:.2f}" )