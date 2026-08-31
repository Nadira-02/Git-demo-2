import random

suorita = True
while suorita:
    print("Tämä printtaantuu vain kerran")
    suorita = False

print("Suoritus loppui.")

luku = 1

while luku <= 5:
    print(luku)
    luku = luku + 1

print("Jatketaan ohjelmaa.")


luku = int(input('Anna luku josta laskema alaspäin: '))

while luku >= 1:
    print(luku)
    luku -= 1

###################

salasana = input('Anna salainen salasana jotta pääset sisään (python):').strip()

while salasana != 'python': 
    print('Väärä salasana')
    salasana = input('Anna salasana uudestaan: ')

print('Tervetuloa sisään, koodi oli oikein.')

#############################

komento = input('Anna komento (lopeta, APUA): ').strip().lower

while komento != 'lopeta':
    if komento == 'APUA' :
        break
    print('Annoit komennon: ', komento)
    komento = input('Anna uusi komento: ')
else:
    print('Annoit käskyn lopeta, joten näin tehdään!!!')

print('ohjelma jatkuu')

##############################

noppa1 = noppa2 = heitot = 0

while (noppa1 != 6 or noppa2 != 6):

    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    print(noppa1, noppa2)
    heitot = heitot + 1

print(f"Tarvittiin {heitot:d} heittoa.")

###########################

eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1

pelikerta = 0
heitot = 0
while pelikerta < 1000:

    noppa1 = noppa2 = 0
    while (noppa1 != 6 or noppa2 != 6):

        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        print(noppa1, noppa2)
        heitot = heitot + 1

    pelikerta += 1
print('Pelikertoja meillä oli:', pelikerta)
print(f'Tarvittiin {heitot:d} heittoa.')
print(f'')



print(f"Tarvittiin {heitot:d} heittoa.")