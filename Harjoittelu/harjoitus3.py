class Kissa:
    def __init__(self, nimi, syntymävuosi, maukuminen="Miau miau"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.maukuminen = maukuminen

    def mauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi +  "maukkuu: " + self.maukuminen)
        return

kissa1 = Kissa("Zaym", 2024)
kissa2 = Kissa("Lili", 2023)

kissa1.mauku(3)
kissa2.mauku(2)




