def interclasare(stanga, dreapta):
    rezultat = []
    i = 0
    j = 0

    while i < len(stanga) and j < len(dreapta):
        if stanga[i] < dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1

    while i < len(stanga):
        rezultat.append(stanga[i])
        i += 1

    while j < len(dreapta):
        rezultat.append(dreapta[j])
        j += 1

    return rezultat
print(interclasare([1, 6, 15, 28, 99], [3, 12, 23, 78, 100]))

# merge sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mijloc = len(lista) // 2
    stanga = merge_sort(lista[:mijloc])
    dreapta = merge_sort(lista[mijloc:])

    return interclasare(stanga, dreapta)
print(merge_sort([98, 32, 1, 19, 6, 65, 4]))  