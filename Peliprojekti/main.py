import os
from Peli.pelaaja01 import Pelaaja
from Peli.kohteet02 import Vesiputous, Temppeli, Kalkkikiviluola
from Peli.tallennus03 import lue_tiedosto, tallenna_peli, lataa_peli

def aloitus():
    print(lue_tiedosto("intro.txt"))
    print(lue_tiedosto("ohjeet.txt"))

    if os.path.exists("tallennus.txt"):
        valinta = input("\nLöytyi tallennettu peli. Haluatko jatkaa sitä (kyllä/ei)? ").strip().lower()
        if valinta == "kyllä":
            pelaaja = lataa_peli("tallennus.txt")
            if pelaaja:
                return pelaaja

    print("\n------ TERVETULOA TROOPPISEN SAAREN SEIKKAILUPELIIN ------")
    nimi = input("\nAnna nimi: ").strip()

    while True: 
        try: 
            ika = int(input("Anna ikä: "))
            break
        except ValueError:
            print("Virhe: syötetty arvo ei ole kokonaisluku. Yritä uudestaan.")

    if ika < 12:
        print("Olet alaikäinen. Ohjelma suljetaan.")
        return None
    else:
        print(f"\nTervetuloa peliin, {nimi}!")
        return Pelaaja(nimi, ika)

def siivous(pelaaja: Pelaaja):
    print("\n=================================")
    print("---ALKUPISTE: SAAREN RANNIKKO ---")
    print("=================================")
    print("Olet rannikolla. Rannalla on muovijätteitä ja roskia.")

    while True:
        try:
            maara = int(input("Kuinka monta roskaa pyrit keräämään rannalta ennen turistien tuloa? "))
            if maara >= 0:
                break
        except ValueError:
            print("Virhe: Syötä numero.")

    pelaaja.keraa(maara)
    print(f"\nErinomaista! Keräsit kaikki {pelaaja.roskien_maara} roskaa rannalta. Nyt ranta on siisti.")
    print(f"Turistilaiva saapuu satamaan!")
    tallenna_peli(pelaaja)

def valitse_reitti(pelaaja: Pelaaja):

    print("\n[MATKA ALKAA!]")
    print("1: Vasen suunta (Kalkkikiviluola)")
    print("2: Keski suunta (Temppeli)")
    print("3: Oikea suunta (Vesiputous)")

    while True:

        valinta = input("Valitse suunta (1, 2 tai 3): ").strip()

        if valinta == "1":
            return Kalkkikiviluola(pelaaja)
        elif valinta == "2":
            return Temppeli(pelaaja)
        elif valinta == "3":
            return Vesiputous(pelaaja)
        else:
            print("Virheellinen valinta! Syötä numero 1, 2 tai 3.")

def main():
    pelaaja = aloitus()
    if pelaaja is None:
        return

    if pelaaja.roskien_maara == 0:
        siivous(pelaaja)
    
    tulos = valitse_reitti(pelaaja)

    print("\n=================================")
    print("---ALKUPISTE: SAAREN RANNIKKO ---")
    print("=================================")
    print(f"Pelaaja: {pelaaja.nimi}")
    print(f"Kerätyt roskat: {pelaaja.roskien_maara}")
    print(f"Inventaario: {pelaaja.inventaario}")
    print(f"Pelin tulos: {tulos}")

    tallenna_peli(pelaaja)

if __name__ == "__main__":
    main()

