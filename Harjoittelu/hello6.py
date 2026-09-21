class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)

class Hoitola:
    def __init__(self):
        self.koirat = []
        

    def koira_sisään(self, koira):
        self.koirat.append(koira)

        print(koira.nimi + 'kirjattu sisään')

        print(koira.hauku(2))

    def koira_ulos(self, koira):
            self.koirat.remove(koira)
    
            print(koira.nimi + 'kirjattu ulos')
    
            print(koira.hauku(2))

    def tervehdi_koiria(self):
        for koira in self.koirat:
            koira.hauku(1)


#Pääohjelma

koira1 = Koira("Muro", 2018)
koira2 = Koira("Rekku", 2022, "Viu viu viu")

hoitola = Hoitola()

hoitola.koira_sisään(koira1)
hoitola.koira_sisään(koira2)

hoitola.tervehdi_koiria()

hoitola.koira_ulos(koira1)
hoitola.tervehdi_koiria()

koira1.hauku(3)
koira2.hauku(2)
koira2 = koira1 # viittaus ensimmäiseen koiraan postuu ja kummatkin muuttujut viittaavat samaan. 
koira2.hauku(1)

hoitola.koira_sisään(Koira("Bella", 2016))

hoitola.koirat[0].hauku(2)

# lista on myös olio ja siihen viitataan muuttujilla.
''''
def muokkaa_listaa(list):
    list.append(6)

lista = (1, 5, 8)
print(lista)
muokkaa_listaa(lista)
print(lista)
'''


