kuha = int(input("Anna kuhan pituus (cm)"))

if kuha < 37:
    print("laske kuha takaisin järveen!!")
    print(f"Sallitusta puuttuu: {37 - kuha}")
else:
    print("Hieno kuha!")

#########
sukupuoli = input("Anna sukupuoli ('nainen' tai 'mies'): ")
hemoglobiini = float(input("Anna hemoglobiini arvo: "))

if sukupuoli == 'nainen':
    if hemoglobiini < 117: 
        print("Hemoglobiini arvo on alhainen.")
    elif hemoglobiini > 175:
        print("Hemoglobiini arvo on suuri.")
    else: 
        print("Hemoglobiini arvo on normaali.")

elif sukupuoli == 'mies':
    if hemoglobiini < 134:
        print("Hemoglobiini arvo on alhainen.")
    elif hemoglobiini > 195:
        print("Hemoglobiini arvo on suuri.")
    else: 
        print("Hemoglobiini arvo on normaali.")
else:
    print("Virheellinen syöttö. Yritä uudelleen.")

###############

           