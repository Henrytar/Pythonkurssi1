name = input("Anna nimesi: ").lower()


if name != "matti" :
    keitot = int(input("Monatko keittoannosta?: "))
    print(f"kokonaishinta on {keitot * 5.90:.2f} euroa.")

else:
    print("Seuraava, kiitos!")
