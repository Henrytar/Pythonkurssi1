def parilliset(lista):
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista


luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9]
karsittu = parilliset(luvut)

print("og lista:", luvut)
print("fixed lista (vain parilliset luvut):", karsittu)
