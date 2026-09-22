class Elain:
    lukumäärä = 0
    def __init__(self, nimi, paino, syntymäaika):
        Elain.lukumäärä = Elain.lukumäärä + 1
        self.numero = Elain.lukumäärä
        self.nimi = nimi
        self.paino = paino
        self.syntymäaika = syntymäaika
        
    def Tulosta_tiedot(self):
        print(f'{self.numero}: {self.nimi}, {self.paino}, {self.syntymäaika}')

    def Liiku(self):
        print(f"{self.nimi} liikkuu jotenkin johonkin.")

class Peto:
    def __init__(self, on_metsastaja):
        self.on_metsastaja = on_metsastaja

class Ilves(Elain):
    def __init__(self, nimi, paino, syntymäaika):
        super().__init__(nimi, paino, syntymäaika)

    def Tulosta_tiedot(self):
        super().Tulosta_tiedot()
        

    def Kilju(self):
        print(f'Ilves nimeltään {self.nimi} karjuu.')

class Karhu(Elain, Peto):
    def __init__(self, nimi, paino, syntymäaika, on_metsastaja):
        Elain.__init__(self, nimi, paino, syntymäaika)
        Peto.__init__(self, on_metsastaja)

    def Tulosta_tiedot(self):
        super().Tulosta_tiedot()
        

    def Talvi(self):
        print(f'Karhu nimeltään {self.nimi} on talvi Horroksessa. Eläin on {self.on_metsastaja}')

elaimet = []
# elaimet(Elain("Joku elukka", 1500, 2025))
# uusi_elain.Liiku()

elaimet.append(Ilves("Ilveskissa", 6500, 2026))
# ilves1.Liiku()
# ilves1.Kilju()

elaimet.append(Karhu("Karhu pentu", 7500, 2011, True))
# karhu1.Liiku()
# karhu1.Talvi()

for t in elaimet:
    t.Tulosta_tiedot()




