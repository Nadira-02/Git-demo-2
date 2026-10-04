def Vesiputous(pelaaja):
    print("\n==========================")
    print("---KOHDE 1: VESIPUTOUS ---")
    print("==========================")
    print("Saavuitte saaren vesiputous kohteeseen.")
    print("Turistit ihailevat saaren luontoa ja vesiputousta.\nTuristit kuvaavat matkamuistoja.")

    input("\nJatka matkaa painamalla'ENTER': ")
    print("Jatketaan matkaa seuraavaan kohteeseen.")


    return Temppeli(pelaaja)
    
def Temppeli(pelaaja):
    print("\n==========================")
    print("---KOHDE 2: TEMPPELI ---")
    print("==========================")
    print("Saavuitte saaren muinaiseen temppeliin.")
    print("Turistit tutustuvat saaren muinaiseen historiaan.")
    print("Torilta saa ostaa matkamuistoja.")

    ostaminen = input("\nHaluatko ostaa matkamuistoja? (kyllä/ei)").strip().lower()

    if ostaminen == "kyllä":
        while True:
            ostos = input("Mitä haluat ostaa?").strip()
            if ostos == "":
                break
            pelaaja.inventaario.append(ostos)
    elif ostaminen == "ei":
        print("Päätät olla ostamatta mitään torilta.")

    input("\nJatka matkaa painamalla'ENTER': ")
    print("Jatketaan matkaa seuraavaan kohteeseen.")
    return Kalkkikiviluola(pelaaja)
    

def Kalkkikiviluola(pelaaja):
    print("\n==========================")
    print("---KOHDE 1: KALKKIKIVILUOLA ---")
    print("==========================")
    print("Saavuitte saaren kalkkikiviluolaan.")
    print("Turistit ihailevat tippukiviä ja erikoisia kivilajeja.")
    print("Matkan varrella kohtaatte kolmeen värilliseen oveen.\nLuolan seinään on kaiverrettu vanha matemaattinen vihje.")
    print("Oikea ovi numero selviää ratkaisemalla yhtälön: ")
    print("\n[6x + 4 = 20 - 2x]")
    print("Mikä on oikea vastaus:\nOvi 1: sininen\nOvi 2: vihreä\nOvi 3: punainen") 

    while True: 
        valinta = input("Valitse oikea numero (1, 2 tai 3): ").strip()
        if valinta == "1":
            print("\n[VÄÄRÄ OVI]")
            print("Oven takana ei ole mitään.")
            print("Game over")
            return "Hävisit"
        elif valinta == "2":
            print("\n[OIKEA OVI]")
            print("Oven takana hehkuu vihreä muinainen kristalli. Onneksi olkoon!\n Löysit harvinainen kristalli.")
            ottaminen = input("Otatko mukaan reppuun? (kyllä/ei): ").strip().lower()
            if ottaminen == "kyllä":
                pelaaja.inventaario.append("Muinainen kristalli")
                print("Otit kristallin mukaan.")
            elif ottaminen == "ei":
                print("Päätit jättää muinaisen kristallin.")

            print("Voitit pelin ja nyt palaatte takaisin rannikkoon.")
            return "Voitit"
        elif valinta == "3":
            print("[VÄÄRÄ OVI]\nOven takana sihisee karmea ääni....SE ON KÄÄRME!!!\nKaikki juoksee pois luolasta.")
            print("Game over")
            return "Hävisit"
        else: 
            print("Virheellinen valinta! Valitse 1, 2 tai 3.\n")





   