def merge_sort(v):
    if len(v) <= 1:
        return v

    mijloc = len(v) // 2

    stanga = merge_sort(v[:mijloc])
    dreapta = merge_sort(v[mijloc:])

    return interclasare(stanga, dreapta)


def interclasare(stanga, dreapta):
    rezultat = []
    i = 0
    j = 0

    while i < len(stanga) and j < len(dreapta):
        if stanga[i] <= dreapta[j]:
            rezultat.append(stanga[i])
            i += 1
        else:
            rezultat.append(dreapta[j])
            j += 1

    rezultat.extend(stanga[i:])
    rezultat.extend(dreapta[j:])

    return rezultat


v = [5, 2, 8, 1, 9, 3]

print("Vectorul sortat este:", merge_sort(v))