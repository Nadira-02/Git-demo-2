# sähkölaskulaskin
kulutus = float(input("\nsyötäsähkökulutus (kWh): "))

hinta = 0

if kulutus <= 50:
    # kWh hinta on aina 10 senttiä
    hinta = kulutus * 10
elif kulutus <= 200:
    # ensimmäiset 50 kWh 10 senttiä ja loput 8
    hinta = 50 * 10
    # ja loput 8 senttiä
    hinta = hinta + (kulutus-50) * 8
else: 
    # ensimmäiset 50 kWh 10 senttiä, seuraavat 150 8 senttiä
    # loput yli 200 kWh 6 senttiä
    hinta = 50 * 10 + 150 * 8 + (kulutus - 200) * 6

# alkuperäinen muoto
print(f"Sähkön hinta: {hinta/100} euroa.")

# Tulostuksen hifistely kotimaiseen muotoon
print(f"Sähkön hinta: {hinta//100:.0f},{hinta%100:.0f} euroa.")