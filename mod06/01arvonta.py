import random

lukumäärä = int(input("Anna arpakuutioiden lukumäärä: "))

summa = 0

for _ in range(lukumäärä):

    silmaluku = random.randint(1, 6)

    summa += silmaluku

print(f"Arpakuutioiden silmälukujen summa on: {summa}.")
