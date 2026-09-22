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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

    def Tulosta_tiedot(self):
            print("\n[SÄHKÖAUTO]")
            print(f"Rekisteritunnus: {self.rekisteritunnus}")
            print(f'Huippunopeus: {self.huippunopeus} km/h')
            print(f'Akkukapasiteetti kWh: {self.akkukapasiteetti} kWh')

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko_litroina):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko_litroina = bensatankin_koko_litroina

    def Tulosta_tiedot(self):
        print("\n[POLTTOMOOTTORIAUTO]")
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f'Huippunopeu: {self.huippunopeus} km/h')
        print(f'Akkukapasiteetti kWh: {self.bensatankin_koko_litroina} l')

auto = Sähköauto("ABC-15", 180, 52.5)
auto1 = Polttomoottoriauto('ACD-123', 165, 32.3)

auto.kiihdytä(120)
auto1.kiihdytä(150)

auto.kulje(3)
auto1.kulje(3)

auto.Tulosta_tiedot()
auto1.Tulosta_tiedot()

print(f"Sähköauton ({auto.rekisteritunnus}) kuljettu matka: {auto.kuljettu_matka} km")
print(f"Polttomoottoriauton ({auto1.rekisteritunnus}) kuljettu matka: {auto1.kuljettu_matka} km")
