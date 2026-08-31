import random

oikea_numero = random.randint(1, 10)

arvaus = int(input('Arvaa numero 1 ja 10 väliltä'))

while arvaus != oikea_numero:
    if arvaus < oikea_numero:
        print('Väärin')
        print('Liian pieni arvaus')
    else:
        print('Liian suuri arvaus')

    arvaus = int(input('Arvaa uudestaan: '))

print(f'Yes, sait kaiken oikein!!! Numero tosiaan oli {oikea_numero} ')
