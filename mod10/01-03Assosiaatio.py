class Hissi:
    def __init__(self, nimi, alin_kerros, ylin_kerros):
        self.nykyinen_kerros = alin_kerros
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nimi = nimi

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros > self.ylin:
            kohdekerros = self.ylin
        elif kohdekerros < self.alin:
            kohdekerros = self.alin

        print(f"Siirrytään kerrokseen {kohdekerros}")
        while self.nykyinen_kerros < kohdekerros:
            self.kerros_ylos()
        while self.nykyinen_kerros > kohdekerros:
            self.kerros_alas()

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi {self.nimi} on nyt kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi{self.nimi} on nyt kerroksessa {self.nykyinen_kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            uusi_hissi = Hissi(f"numero {i+1}", alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissia(self, numero, kohdekerros):
        #hissi numero yksi on listalla indeksissa 0
        self.hissit[numero-1].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("palohalytys!!!")
        for h in self.hissit:
            h.siirry_kerrokseen(h.alin)

talo = Talo(1, 10, 3)
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)

hissi1 = Hissi("Pääaula",  1, 12)
hissi2 = Hissi("Henkilökunta", 5, 20)

hissi1.siirry_kerrokseen(4)
hissi2.siirry_kerrokseen(8)

talo.palohalytys()