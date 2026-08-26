pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Laske kuha takaisin järveen!")
    print(f"Se on {puuttuu} senttiä alamittainen.")
else:
    print("Hieno kuha, voit pitää sen!")
    

