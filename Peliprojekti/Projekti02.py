import sys

def tulosta_valikko():
    print("\n--- Valikko ---")
    print("Komennot: ohje, tila, tervehdi, lopeta")

print("Tervetuloa!")

Ikä = int(input("Anna ikäsi: "))

if Ikä < 12:
    print("Olet alaikäinen. Ohjelma suljetaan.")
    sys.exit()
else:
    print("Tervetuloa peliin!")

while True:
    tulosta_valikko()
    komento = input("Syötä komento: ").strip().lower()

    if komento == "lopeta":
        print("Ohjelma sammuu. Heippa!")
        break
    elif komento == "ohje":
         print("Syötä komentoja valinkon mukaan.")
    elif komento == "tila":
        print("Kaikki järjestelmät toimivat normaalisti.")
    elif komento == "tervehdi":
        print("Heippa hei! Mukava nähdä.")
    else:
        print("Virhe. Yritä uudelleen.")
        

    