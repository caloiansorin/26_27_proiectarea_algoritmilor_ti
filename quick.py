def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]

    stanga = [x for x in lista if x < pivot]
    mijloc = [x for x in lista if x == pivot]
    dreapta = [x for x in lista if x > pivot]

    return quick_sort(stanga) + mijloc + quick_sort(dreapta)


numere = [8, 3, 1, 7, 0, 10, 2]

print(quick_sort(numere))