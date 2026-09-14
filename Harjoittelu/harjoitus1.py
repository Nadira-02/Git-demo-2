ikä = int(input("Anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))
if ikä >= 18 or (ikä >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")
else:
    print("lääke ei ole sallittu.")
#################

# esimerkki tehtävä:
import random

toistot = 0
heitot_yhteensä = 0

while toistot < 10000:
    noppa1 = noppa2 = heitot = 0
    while (noppa1 > 2 or noppa2 != 6):
        noppa1 = random.randint(1, 6)
        noppa2 = random.randint(1, 6)
        heitot = heitot + 1
# break ei tarvii koska koodissa en käytä while true:
       # if noppa1 <= 2 and noppa2 == 6:
            #break

    toistot = toistot + 1
    heitot_yhteensä = heitot_yhteensä + heitot

heitot_keskimäärin = heitot_yhteensä / toistot
print(f"Heitot keskimäärin: {heitot_keskimäärin:.2f}")    


#####################

ostoslista = []
komento = input("Anna komento: ")
while komento != "":
    ostoslista.append(komento)
    komento = input("Anna komento: ")

for tuote in ostoslista:
    print(f"{tuote}, on hyvä valinta.")

#################


luku = int(input("Anna luku: "))
for i in range(1, 11):
    tulos = luku * i
    print(f"{luku} * {i}: {tulos}")
