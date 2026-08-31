tuuma_cm = 2.54

tuumat = float(input("Anna tuumat: "))

while tuumat >= 0:
    senttimetrit = tuumat * tuuma_cm
    print(f"{tuumat} tuuma on {senttimetrit} senttimetriä.")
    tuumat = float(input("Anna uudet tuumat: "))
if tuumat <= 0:
    print("Ohjelma lopetettu.")
    

