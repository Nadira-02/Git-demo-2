viikonpaivat = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
print(viikonpaivat)
print("ensimmäinen viikonpäivä on", viikonpaivat[0])

print("\narkipäivät ja viikonlopun päivät ovat omissa monikoissaan samassa monikossa:")
viikonpaivat_v2 = [("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai"), ("lauantai", "sunnuntai")]
print(viikonpaivat_v2)
print("arkipäivät ovat", viikonpaivat_v2[0])
print("viikonlopun päivät ovat", viikonpaivat_v2[1])
print("ensimmäinen viikonpäivä on", viikonpaivat_v2[0][0])

(eka, toka, kolams, neljas, viides, kuudes, seitsemas) = viikonpaivat
print(eka, toka, viides, seitsemas)


import random

print("\nTuplanoppa")

def heita():
    return (random.randint(1, 6), random.randint(1, 6))

nopat = heita()
print(nopat)
print(f"Nopista tuli {nopat[0]} ja {nopat[1]}.")

print("\nJoukkoja")
viikonpaivat = {"maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"}
print(viikonpaivat)

viikonpaivat.add("extrapaiva")
viikonpaivat.add("extrapaiva")
for paiva in viikonpaivat:
    print(paiva)
viikonpaivat.remove("keskiviikko")
print(viikonpaivat)

#################

numerot = {"Viivi": "050-1234567",
           "Ahmed": "040-1112223",
           "Pekka": "050-7654321"}

numerot["Olga"] = "050-101012"
numerot["Mary"] = "0401-2132139"

numerot["Pekka"] = "poistettu"

numerot["Ahmed"] = "050-123456"

print(numerot)
print("Olgan numero on", numerot["Olga"])

#nimi = input("Anna nimi: ")
nimi = "Pekka"
if nimi in numerot:
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")

players = [
    {     "name": "Player 1",
          "skill_level":10,
          "inventory": {"nap", "knife"}
    },

    {     "name": "Player 2",
          "skill_level":20,
          "inventory": {"axe"}
    }
]

for player in players:
    #print(player)
    print(f"Pelaaja {player['name']} taitotaso on {player['skill_level']}, hallussa:")
    for item in player["inventory"]:
        print(f"- {item}")
