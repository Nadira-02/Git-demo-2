def karsi_parittomat(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

lista = [11, 13, 22, 1, 3,  4, 24, 2]

karsittu_lista = karsi_parittomat(lista)

print(f"lista: {lista}")
print(f"karsittu lista: {karsittu_lista}")



