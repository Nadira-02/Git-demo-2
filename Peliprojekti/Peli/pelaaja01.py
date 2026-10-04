class Pelaaja:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.inventaario = ["Taskulamppu", "Kompassi", "Juomapullo", "Eväät"]
        self.roskien_maara = 0

    def keraa(self, maara):
            self.roskien_maara += maara
            print(f'Hyvä keräsit {maara} roskaa.\nKerätty yhteensä: {self.roskien_maara}')

    def lisaa_esine(self, esine: str):
         self.inventaario.append(esine)

        

