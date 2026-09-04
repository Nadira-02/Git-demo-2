import time

Kaupungit = []

print("Anna viiden kaupungin nimet: ")

for i in range(5):
    Kaupunki = input(f"Anna kaupunki {i + 1}: ")
    Kaupungit.append(Kaupunki)

print("\nAntamasi kaupungit olivat:")

for Kaupunki in Kaupungit:
    print(Kaupunki)
    time.sleep(1)
