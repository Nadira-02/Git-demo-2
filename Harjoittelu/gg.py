oikea_numero = 2

arvaus = int(input('Arvaa numero (1, 2 ja 3): '))

while arvaus != oikea_numero:
    if arvaus == 1:
        print('Väärin Ovi')
        print('Väärä ovi: Oven takana ei ole mitään. Game Over!')
    elif arvaus == 3:
        print('Väärä Ovi')
        print('Avaat oven ja kuulette sihisevää ääntä... Luolakäärme herää ja hyökkää! Teidän täytyy paeta luolasta!')
    else:
        print('Virheellinen arvaus.')

    arvaus = int(input('Arvaa uudestaan: '))

print(f'Avaat oven ja näet hehkuvan valon! Löysitte aarteen! Turistit taputtavat ja saari on pelastettu! {oikea_numero} ')