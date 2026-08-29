Vuosiluku = int(input("Anna vuosiluku: "))

if Vuosiluku % 400 == 0:
    print(f"Vuosi {Vuosiluku} on karkausvuosi.")
elif Vuosiluku % 100 == 0:
    print(f"Vuosi {Vuosiluku} ei ole karkausvuosi.")
elif Vuosiluku % 4 == 0:
    print(f"Vuosi {Vuosiluku} on karkausvuosi.")
else: 
    print(f"Vuosi {Vuosiluku} ei ole karkausvuosi.")