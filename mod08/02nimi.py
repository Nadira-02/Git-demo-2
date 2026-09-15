nimet = set()

while True:
    nimi = input('Anna nimi: ')

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiempi nimi on syötetty.")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("\nSyötetyt nimet:")
for n in nimet:
    print(n)
    