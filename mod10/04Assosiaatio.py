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


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nTilanne kilpailussa: {self.nimi}")
        print(f"{'Rekisteritunnus':<20} {'Huippunopeus (km/h)':<20} {'Nopeus (km/h)':<15} {'Kuljettu matka (km)':<20}")
        print("-" * 75)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<20} {auto.huippunopeus:<20} {auto.nopeus:<15} {auto.kuljettu_matka:<20}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False


osallistujat = []
for i in range(1, 11):
    huippu = random.randint(100, 200)
    tunnus = f"ABC-{i}"
    osallistujat.append(Auto(tunnus, huippu))

romuralli = Kilpailu("Suuri romuralli", 8000, osallistujat)

tunnit = 0

while not romuralli.kilpailu_ohi():
    romuralli.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        print(f"\n>>> {tunnit} tuntia kulunut <<<")
        romuralli.tulosta_tilanne()

print(f"\n======== KILPAILU PÄÄTTYI! Kesto: {tunnit} h ========")
romuralli.tulosta_tilanne()