def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mijloc = len(lista) // 2

    stanga = merge_sort(lista[:mijloc])
    dreapta = merge_sort(lista[mijloc:])

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

    rezultat += stanga[i:]
    rezultat += dreapta[j:]

    return rezultat

numere = [ 6, 1, 3, 9, 0]
print("Lista nesortată:", numere)
print("Lista sortată:", merge_sort(numere))

# Împărțim lista în două jumătăți, jumatatile in jumatati etc etc până când ajungem la subliste de un singur element
# Recreem lista de jos in sus, punand numerele din perechi in ordine crescatoare
# La impartire, partea intreaga ramane mereu in partea stanga 
#    6   1   3   9   0
#          |
#        /   \
#    6  1     3  9  0
#    / \       / \
#   6   1     3   9  0
#   |   |     |    / \
#   6   1     3   9   0
#                  \ /
#                  0 9
#   \ /        \   /
#   1 6        0 3 9
#     \          /
#      0 1 3 6 9 
