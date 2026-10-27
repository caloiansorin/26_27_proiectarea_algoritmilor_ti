def quick_sort(lista):

    pivot = lista[len(lista) // 2]

    mai_mici = [x for x in lista if x < pivot]
    egale = [x for x in lista if x == pivot]
    mai_mari = [x for x in lista if x > pivot]

    
    return quick_sort(mai_mici) + egale + quick_sort(mai_mari)


numere = [8, 2, 1, 3, 5, 4]

rezultat = quick_sort(numere)
print("Lista sortata:", rezultat)

# Se alege pivot de referinta (mijlos - in ex, dar se poate si primul sau ultimul element)
# Pivotul se plaseaza la mijloc, iar elementele mai mici decat pivotul se plaseaza in stanga, iar cele mai mari in dreapta 
#     I el <   II el < ....     pivot     I el >  II el > ....
