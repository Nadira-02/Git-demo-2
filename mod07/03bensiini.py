def gallona_litroiksi(gallonat):
    return gallonat * 3.785

def pääohjelma():
    while True:
        gallonat = float(input("Anna bensiinin määrä gallonoina: "))

        if gallonat < 0:
            print("Ohjelma lopetettu.")
            break

        litrat = gallona_litroiksi(gallonat)
        print(f"{gallonat} gallonaa on {litrat: .2f} litraa.\n")

pääohjelma()
