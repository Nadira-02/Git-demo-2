class Pelaaja:
    def __init__(self, nimi: str, ika: int):
        self.nimi = nimi
        self.ika = ika
        self.inventaario = ["Taskulamppu", "Kompassi", "Juomapullo", "Eväät"]
        self.roskien_maara = 0

    def keraa(self, maara: int):
            self.roskien_maara += maara
            print(f'Hyvä keräsit {maara} roskaa.\nKerätty yhteensä: {self.roskien_maara}')

    def lisaa_esine(self, esine):
         self.inventaario.append(esine)

        

