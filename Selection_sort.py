def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        minim = i

        for j in range(i + 1, n):
            if lista[j] < lista[minim]:
                minim = j

        lista[i], lista[minim] = lista[minim], lista[i]

    return lista

numere = [6, 1, 3, 9, 0]
print("Lista nesortată:", numere)
selection_sort(numere)
print("Lista sortată:", numere)

# Primul element din lista este considerat minim initial, caut in elementele ramase, daca exista alt minim swap(min initial, min gasit)
# Împărțim vizual lista în două părți: partea sortata (stanga) și partea nesortata (dreapta)
# In lista nesortata, caut cel mai mic element si il aduc in fata listei nesortate / la coada listei sortate
# 6 1 3 9 0 
# 0 [ 1 3 9 6 ]
# 0 1 [ 3 9 6 ]
# 0 1 3 [ 9 6]       caut elemnetele mai mici, cele mai mari trec peste ele 
# 0 1 3 6 9
