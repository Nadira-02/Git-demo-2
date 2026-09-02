import random

x = random.uniform(-1,1)
y = random.uniform(-1,1)

piste = [x, y]

print(piste)

print(piste[0])

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

print(nimet[-2])
print(nimet[1:3])
print(nimet[2:])
print(nimet)

listan_koko = len(nimet)
print(listan_koko)

counter = 0
while counter < len(nimet):
    print(f"{counter+1}. nimi: {nimet[counter]}")
    counter += 1

nimet.append("Joku uusi nimi")
nimet.insert(4, "Teppo")
print(nimet, len(nimet))

todos = []
todos.append("Tee läksyt!")
new_todo = input("Anna uusi tehtävä: ")
todos.append(new_todo)

for todo in todos:
    print(todo)

for number in range(len(todos)):
    print(todos[number])

for luku in range(3, 31, 3):
    print(luku)