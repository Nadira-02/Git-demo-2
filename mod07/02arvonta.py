import random

print("\n=== Noppapeli ===")
def heita_noppaa(tahkojen_lkm):
    return random.randint(1, tahkojen_lkm)

nopan_koko = int(input("Anna nopan koko (maksimisilmäluku): "))

silmaluku = 0
while silmaluku != nopan_koko:
    silmaluku = heita_noppaa(nopan_koko)
    print(silmaluku)