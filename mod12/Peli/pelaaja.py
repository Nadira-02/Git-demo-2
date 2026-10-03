class Pelaaja: 
    def __init__(self, nimi):
        self.nimi = nimi 

    def hauku(self):
        print(f"{self.nimi}: Oot tyhmä!")

pelaaja1 = Pelaaja("Nadira")
pelaaja1.hauku()
