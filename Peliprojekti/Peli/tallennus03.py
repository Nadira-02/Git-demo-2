import os
from Peli.pelaaja01 import Pelaaja


def lue_tiedosto(tiedoston_nimi: str) -> str:
    if os.path.exists(tiedoston_nimi):
        with open(tiedoston_nimi, "r", encoding="utf-8") as f:
            return f.read()
    return f"Tiedostoa {tiedoston_nimi} ei löytynyt."


def tallenna_peli(pelaaja: Pelaaja, tiedoston_nimi: str = "tallennus.txt"):
    try:
        with open(tiedoston_nimi, "w", encoding="utf-8") as f:
            f.write(f"{pelaaja.nimi}\n")
            f.write(f"{pelaaja.ika}\n")
            f.write(f"{pelaaja.roskien_maara}\n")
                    
            f.write(f"{','.join(pelaaja.inventaario)}\n")

        print(f"\n[Pelitilanne tallennettu tiedostoon {tiedoston_nimi}]")
    except Exception as e:
        print(f"Tallennus epäonnistui: {e}")


def lataa_peli(tiedoston_nimi: str = "tallennus.txt") -> Pelaaja:
    if not os.path.exists(tiedoston_nimi):
        print("Tallennettua peliä ei löytynyt.")
        return None

    try:
        with open(tiedoston_nimi, "r", encoding="utf-8") as f:
            rivit = [rivi.strip() for rivi in f.readlines()]
            nimi = rivit[0]
            ika = int(rivit[1])
            roskat = int(rivit[2])

            pelaaja = Pelaaja(nimi, ika)
            pelaaja.roskat_keratty = roskat

            if len(rivit) > 3 and rivit[3]:
                pelaaja.inventaario = rivit[3].split(",")

            print(f"\n[Ladattiin tallennettu peli: Pelaaja {pelaaja.nimi}]")
            return pelaaja
    except Exception as e:
        print(f"Tallennuksen lataus epäonnistui: {e}")
        return None