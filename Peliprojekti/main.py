from Peli import Pelaaja
from Peli import Vesiputous, Temppeli, Kalkkikiviluola

def aloitus():
    print("------ TERVETULOA TROOPPISEN SAAREN SEIKKAILUPELIIN ------")
    nimi = input("Anna nimi: ").strip()

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
        print(f"\nTervetuloa peliin, {pelaaja.nimi}!")
        return Pelaaja(nimi, ika)

def siivous(pelaaja):
    print("\n==========================")
    print("---ALKUPISTE: SAAREN RANNIKKO ---")
    print("==========================")
    print("Olet rannikolla. Rannalla on muovijätettä ja roskia.")

    while True:
        try:
            maara = int(input("Kuinka monta roskaa pyrit keräämään rannalta ennen turistien tuloa? "))
            if maara >= 0:
                break
        except ValueError:
            print("Virhe: Syötä numero.")

    pelaaja.keraa(maara)
    print(f"\nHyvä! Keräsit kaikki {pelaaja.roskia_maara} roskaa rannalta.")
    print(f"Turistilaiva saapuu satamaan!")

def valitse_reitti(pelaaja):
    print("[MATKA ALKAA!]")
    print("1: Vasen suunta (Kalkkikiviluola)")
    print("2: Keski suunta (Temppeli)")
    print("3: Oikea suunta (Vesiputous)")

    valinta = input("Valitse suunta (1, 2 tai 3): ").strip()

    if valinta == "1":
        return Kalkkikiviluola(pelaaja)
    elif valinta == "2":
        return Temppeli(pelaaja)
    elif valinta == "3":
        return Vesiputous(pelaaja)
    else:
        print("Virheellinen valinta! Syötä numero 1, 2 tai 3.")



## ---PÄÄOHJELMA--- ##
pelaaja = aloitus() 

