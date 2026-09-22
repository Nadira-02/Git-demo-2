def tulosta_ohje():
    print("\n[OHJE]")
    print("Tutki Islannin luolia ja etsi vihjeen avulla aarre.")

def listaa_esine(inventaario_lista):
    print("\n[LÖYSIT ESINEEN!]")
    uusi_esine = input("Haluatko ottaa mukaan löytämäsi esineen?").strip()

    if uusi_esine:
        inventaario_lista.append(uusi_esine)
        print(f'Kyllä otan {uusi_esine} mukaan reppuun!')

    else:
        print('En ota mukaan.')

def näytä_inventaario(inventaario_lista):
    print("\n[INVENTAARIO]")
    if not inventaario_lista:
        print("Reppusi on tyhjä.")
    else: 
        print("Inventaariossasi on: ")
        for esine in inventaario_lista:
            print(f"- {esine}")
def katso_vihje():
    print("\n[VIHJE]")
    print("Vihje on: Kolme eri väristä ovea. (Punainen, Keltainen ja Vihreä).")

Ikä = int(input("Anna ikäsi: "))

if Ikä < 12:
    print("Olet alaikäinen. Ohjelma suljetaan.")
else:
    print("\nTervetuloa peliin!")

    omaisuus = ["Taskulamppu", "Kompassi", "Juomapullo", "Eväät"]

    Pelataan = True
    while Pelataan:
        print("\n--- PÄÄVALIKKO ---")
        print("Komennot: Ohje, Inventaario, Vihje, Kerää, Lopeta")
        komento = input("Syötä komento: ").strip().lower()

        if komento == "lopeta":
            print("Game Over. Kiitos pelaamisesta!")
            Pelataan = False
        elif komento == "ohje":
            tulosta_ohje()
        elif komento == "kerää":
            listaa_esine(omaisuus)
        elif komento == "inventaario":
            näytä_inventaario(omaisuus)
        elif komento == "vihje":
            katso_vihje()
        else:
            print("Virhe. Yritä uudelleen.")
        