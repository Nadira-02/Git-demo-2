class Pelaaja:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.inventaario = ["Taskulamppu", "Kompassi", "Juomapullo", "Eväät"]
        self.roskien_maara = 0

    def keraa(self, kerrat):
        for i in range(kerrat):
            self.roskien_maara += 1
            print(f'Hyvä keräsit kaikki roskat!\nKerätty roska yhteensä: {self.roskien_maara}')

        

