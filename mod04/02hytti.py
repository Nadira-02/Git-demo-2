hyttiluokka = input("Anna laivan hyttiluokka (LUX, A, B, C): ").upper()

if hyttiluokka == "LUX":
    print("LUX on parvekkeelinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti yläkannella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

