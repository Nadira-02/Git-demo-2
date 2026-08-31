luvut = []

while True:
    luku = input("Anna luku: ")

    if luku == "":
        break
    luku1 = float(luku)
    luvut.append(luku1)

if len(luvut) > 0:
    pienin = min(luvut)
    suurin = max(luvut)

    print(f"Antamistasi luvuista pienin oli: {pienin}")
    print(f"Antamistasi luvuista suurin oli: {suurin}")
else:
    print("Et antanut yhtään lukua.")
