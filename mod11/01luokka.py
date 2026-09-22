class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailia = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f'Kirjailija: {self.kirjailia}')
        print(f'Sivumäärä: {self.sivumaara} sivua.')

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f'Lehti: {self.nimi}')
        print(f'Päätoimittaja: {self.päätoimittaja}')

kirja = Kirja("Hytti n:o 6", 'Rosa Liksom', 200)
kirja.tulosta_tiedot()

lehti = Lehti("Aku Ankka", "Aki Hyyppä")
lehti.tulosta_tiedot()

