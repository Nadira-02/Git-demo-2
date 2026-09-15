lentoasemat = {}

while True: 
    print("\nValitse toiminto:")
    print("1 = Syötä uusi lentoasema")
    print("2 = Hae lentoaseman tiedot")
    print("3 = Lopeta")

    valinta = input("Valintasi (1-3): ")

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
        nimi = input("Anna lentoaseman nimi: ").strip()
        lentoasemat[icao] = nimi
        print(f"Lentoasema '{nimi}' ({icao}) tallennettu.")

    elif valinta == "2":
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ").strip().upper()
        if icao in lentoasemat:
            print(f"ICAO-koodia {icao} vastaa lentoasema: {lentoasemat[icao]}")
        else:
            print(f"Tiedot puuttuvat: ICAO-koodilla '{icao}' ei löytynyt lentoasemaa.")

    elif valinta == "3":
        print("Kiitos ja näkemiin!")
        break

    else:
        print("Virheellinen valinta! Syötä numero 1, 2 tai 3.")