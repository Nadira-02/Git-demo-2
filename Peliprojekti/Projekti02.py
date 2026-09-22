Ikä = int(input("Anna ikäsi: "))

if Ikä < 12:
    print("Olet alaikäinen. Ohjelma suljetaan.")
else:
    print("\nTervetuloa peliin!")

    Pelataan = True
    while Pelataan:
        print("\n--- PÄÄVALIKKO ---")
        print("Komennot: Ohje, Inventaario, Vihje, Lopeta")
        komento = input("Syötä komento: ").strip().lower()

        if komento == "lopeta":
            print("Game Over. Kiitos pelaamisesta!")
            Pelataan = False
        elif komento == "ohje":
            print("Etsi aarre vihjeen avulla.")
        elif komento == "vihje":
            print("Kolme eri väristä ovea.")
        elif komento == "inventaario":
            print("Sinulla on taskulamppu, kompassi, juomapullo ja eväät.")
        else:
            print("Virhe. Yritä uudelleen.")
        

    