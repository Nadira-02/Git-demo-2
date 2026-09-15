def summa(luvut):
    s = 0
    for i in luvut:
        s += i
    return s

numerot = [2, 6, 10, 4, 20]

tulos = summa(numerot)

print(f"Lista: {numerot}")
print(f"Listan lukujen summa: {tulos}")
