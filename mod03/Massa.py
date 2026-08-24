leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))

yhteensa_luoteja = (leiviskat * 640) + (naulat * 32) + luodit
yhteensa_grammoja = yhteensa_luoteja * 13.3

kilogrammat = int(yhteensa_grammoja // 1000)
grammat = yhteensa_grammoja % 1000

grammat = round(grammat, 2)

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat} grammaa.")
