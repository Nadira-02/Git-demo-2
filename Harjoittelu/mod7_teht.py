import random

def heita_noppaa(tahkojen_lkm):
    return random.randint(1, tahkojen_lkm)

def noppapeli():
    print("\n=== Noppapeli ===")
    nopan_koko = int(input("Anna nopan koko (maksimisilmäluku): "))
    silmaluku = 0
    heittolaskuri = 0
    while silmaluku != nopan_koko:
        heittolaskuri += 1
        silmaluku = heita_noppaa(nopan_koko)
        print(silmaluku)
    print(f"Heittäessä {nopan_koko}-tahkoista noppa, meni {heittolaskuri} heittoa, jotta saat {nopan_koko}")



while True:
    komento = input("Anna komento>> ")
    if komento == "lopeta":
        print("heippa!")
        break
    elif komento == "noppa":
        noppapeli()
    else:
        print("en ymmärtänyt!")
