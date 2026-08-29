Sukupuoli = input("Anna biologinen sukupuoli (nainen / mies): ").lower()
Hemoglobiini = float(input("Anna hemoglobiiniarvo (g/l): "))

if Sukupuoli == "nainen":
    if Hemoglobiini < 117:
        print("Hemoglobiini on alhainen.")
    elif Hemoglobiini <= 175:
        print("Hemoglobiini on normaali.")
    else:
        print("Hemoglobiini on korkea.")
if Sukupuoli == "mies":
    if Hemoglobiini < 134:
        print("Hemoglobiini on alhainen.")
    elif Hemoglobiini <= 195:
        print("Hemoglobiini on normaali.")
    else: 
        print("Hemoglobiini on korkea.")