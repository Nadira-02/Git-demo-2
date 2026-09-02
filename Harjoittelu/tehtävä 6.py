import random

N = 1000
n = 0
counter = 0

while counter < N:
    counter += 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(f"{counter}. arvotun pisteen koordinaatit, x: {x}, y: {y}")
    if x ** 2 + y ** 2 > 1: 
        n = n + 1
        print("Piste on ympyrän sisällä.")

print(f"Pisteitä arvottu yhteensä {N}, joista ympyrän sisälle osui {n} kpl.")

#Todo: laske pii annetulla kaavalla ja tulosta. kokeile myös eri N arvolla.



