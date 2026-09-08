käyttäjä = input('Anna nimesi: ')
print("Hauska tavata, "+ käyttäjä + "!")

Väri = "Vihreä"

print("Hauska tavata, " + käyttäjä + "!")

# Perustyypit: merkkijono (string), luku (number), joka voi olla kokonaisluku (int), liukuluku (float) tai kopleksiluku, totuusarvo (boolean, joka voi olla true tai false)
# Muut pythonin tietorakenteet: lista (list), monikko (tuple) ja sanakirja (dictionary).

# \n = rivinvaihto

eka = -4 + 2j

print(eka.imag)

# yhteenlasku (+)
# vähennyslasku (-)
# kertolasku (*)
# jakolasku (/), (%)
# kokonaisosan palauttava jakolasku (//)
# potenssi (**)

# esim.
fahrenheit_str = float(input("Anna lämpötila Fahrenheit-asteina: "))
celsius = (fahrenheit_str - 32) * 5/9
print("Lämpötila Celsius- asteina: " + str(celsius))

# f = eli muotoiltu teksti. muuttujat voidaan sijoittaa merkkijonoon ilman + merkkiä ja muita merkkejä kuten str.

hinta = 12.3456

# Tulostetaan käyttäen :10.1f -muotoilua
print(f"Hinta: '{hinta:10.1f}'")
# 6 vvälilyöntiä ja 4 merkkiä = 10


import math

print(f"{'Pii':12s}:{math.pi:10.5f}")
print(f"{'Neperin luku':12s}:{math.e:10.5f}")

Pii         :   3.14159
Neperin luku:   2.71828

