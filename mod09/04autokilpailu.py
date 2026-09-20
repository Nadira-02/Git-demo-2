import random
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):    
        self.kuljettu_matka += self.nopeus * tunnit

autot = []
for i in range(1, 11):
    huippu = random.randint(100, 200)
    tunnus = f"ABC-{i}"
    uusi_auto = Auto(tunnus, huippu)
    autot.append(uusi_auto)

kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynissa = False
            break
print(f"{'Rekisteritunnus':<20} {'Huippunopeus (km/h)':<20} {'Nopeus (km/h)':<15} {'Kuljettu matka (km)':<20}")
print("-" * 75)

for auto in autot:
    print(f"{auto.rekisteritunnus:<20} {auto.huippunopeus:<20} {auto.nopeus:<15} {auto.kuljettu_matka:<20}")
    