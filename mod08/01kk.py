vuodenajat = (
    "talvi", "talvi", "kevät", "kevät", "kevät",
    "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi"
)

kk_numero = int(input("Anna kuukauden numero: "))

if 1 <= kk_numero <= 12:
    vuodenaika = vuodenajat[kk_numero - 1]
    print(f"{kk_numero}. kuukauden vuodenaika on {vuodenaika}.")
else:
    print("Virheellinen kuukauden numero! Syötä luku väliltä 1-12.")