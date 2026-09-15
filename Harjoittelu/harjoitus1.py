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

###############
def tervehdi():
    print("Moi!")

print("Päivä alkaa tervehdyksellä.")
tervehdi()
print("Sitten siirrytään muihin asioihin.")

############
def tervehdi(nimi):

    print(f"Moi, {nimi}!")

tervehdi("Ville")

###############
def neliosumma(eka, toka):
    ns = eka**2 + toka**2
    return ns

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
tulos = neliosumma(luku1, luku2)
print(f"Lukujen {luku1:.3f} ja {luku2:.3f} neliösumma on {tulos:.3f}.")

#################

def laske_keskiarvo(*luvut):
    s = 0
    for i in luvut:
        s += i
    keskiarvo = s / len(luvut)
    return keskiarvo

tulos = laske_keskiarvo(2, 4, 6, 8)
print(f'Lukujen keskiarvo on: {tulos:.2f}')

###############
numerot = {"Nadira": "054-3672873",
           "Magi": "926-39839028"}
print(numerot)

nimi = input("Anna nimi: ")
if nimi in numerot:
    print(f'Henkilön {nimi} puhelinnumero on: {numerot[nimi]}.')
    
#####################

Pääkaupungit = {}

while True:
    print("\nValitse toiminto:")

    print("1: Lisää tiedot: ")
    print("2: Hae tieto: ")
    print("3: Lopeta: ")

    valinta = input("Valitse toiminnot (1-3): ").strip

    if valinta == "1":
        valtion_nimi = input("Anna valtion nimi:").strip().title()
        kaupunki = input("Syötä kaupunki: ").strip().title()

        Pääkaupungit[valtion_nimi] = kaupunki
    elif valinta == "2":
        valtio = input("Syötä valtio: ").strip().title()
        if valtio in Pääkaupungit:
            print(f"kyseisen valtion pääkaupunki on: {Pääkaupungit[valtio]} ")
        else: 
            print("Valtio ei löydy")
    elif valinta == "3":
        print("Kiitos ja Näkemiin!!!")
        break
    else: 
        print("Virheellinen syöttö")

