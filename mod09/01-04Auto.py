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


def moikka():
    print('Tämäpä on mukavaa')


auto = Auto('ABC-123', 142)

print('Auton rekisteritunnus:', auto.rekisteritunnus)
print('Huippunopeus:', auto.huippunopeus)
print('Nopeus:', auto.nopeus)
print('Kuljettu matka:', auto.kuljettu_matka)

moikka()
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print('Auton nopeus kiihdytyksen jälkeen:', auto.nopeus)
auto.kulje(1.5)
print('kuljettu matka 1.5h jälkeen:', auto.kuljettu_matka)

auto.kiihdytä(-200)
print('Auton nopeus jarrutuksen jälkeen:', auto.nopeus)
