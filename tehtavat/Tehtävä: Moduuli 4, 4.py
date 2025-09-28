import random
print("arvaa luku väliltä 1-10!!")
arva = random.randint(1, 10)

while True:
    arva1 = float(input("Anna arvaus: "))

    if arva1 == 0:
        print("Täh")

    elif 0 < arva1 < arva:
        print("liian pieni arvaus!!!")

    elif arva1 > arva:
        print("liaan suuri arvaus!!!")

    if arva1 == arva:
        print("Onneksi olkoon!!")
        break

