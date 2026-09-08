print("print on Pythonin sisäänrakennettu funktio")

def do_nothing():
    pass

do_nothing()

'''''''''
def print_list_of_numbers():
    print(1)
    print(2)
    print(3)

print_list_of_numbers()
print_list_of_numbers()
'''



def print_list_of_numbers(start, end):
    print(f"Tulostettava väli: {start}, {end}")
    for i in range(start, end+1, 1):
        print(i)
    return

print_list_of_numbers(1, 5)
test_return_value = print_list_of_numbers(7, 11)
print("test retunt value", test_return_value)

number = "01"
print(int(number))

def create_list_of_number(start, end):
    print(f"Tehdään lista, jossa arvot: {start}-{end}")
    number_list = []
    for i in range(start, end+1, 1):
        number_list.append(i)
    return number_list

print(create_list_of_number(3, 7))

list_of_numbers = create_list_of_number(11, 16)



def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat:")
    for t in tavarat:
        print("- " + t)

    tavarat.clear()
    return

reppu = ["Vesipullo", "Kartta", "Kompassi"]
inventaario(reppu)
reppu.append("Linkkuveitsi")
inventaario(reppu)

def tulosta_luku(a):
    print(a)
    a = 0

b = 3
tulosta_luku(b)
tulosta_luku(b)

print()

def summa(*luvut):
    print("Syötetyt arvot: ", luvut)
    s = 0
    for i in luvut:
        s += 1
    return s
print("Summa on", summa(1, 2, 3))

