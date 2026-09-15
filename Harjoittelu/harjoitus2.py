Pääkaupungit = {}

while True:
    print("\nValitse toiminto")
    print("1: Lisää tiedot")
    print("2: Hae tieto")
    print("3: Lopeta")

    valinta = input("Valitse toiminnot (1-3): ").strip()

    if valinta == "1":
        valtion_nimi = input("Anna valtion nimi:").strip().title()
        kaupunki = input("Syötä kaupunki: ").strip().title()

        Pääkaupungit[valtion_nimi] = kaupunki
    elif valinta == "2":
        valtio = input("Syötä valtio: ").strip().title()
        if valtio in Pääkaupungit:
            print(f"kyseisen valtion pääkaupunki on: {Pääkaupungit[valtio]} ")
        else: 
            print("Valtio ei löydy")

    elif valinta == "3":
        print("Kiitos ja Näkemiin!!!")
        break

    else: 
        print("Virheellinen syöttö")
        
