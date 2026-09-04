Kokonaisluku = int(input("Anna kokonaisluku: "))

on_alkuluku = True

if Kokonaisluku <= 1:
    print(f"{Kokonaisluku} ei ole alkuluku.")
else:

     for i in range(2, Kokonaisluku):
         if Kokonaisluku % i == 0:
             on_alkuluku = False
             break
         i += 1
if on_alkuluku:
    print(f"Luku {Kokonaisluku} on alkuluku.")
else:
    print(f"Luku {Kokonaisluku} ei ole alkuluku.")
