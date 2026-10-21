def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numere = [5, 1, 4, 2, 8]
print("Lista nesortată:", numere)
bubble_sort(numere)
print("Lista sortată:", numere)

# luam cate doua elemente consecutive din lista, daca sunt in ordine gresita, le interschimbam
# 5 1 4 2 8
# 1 5 4 2 8
# 1 4 5 2 8
# 1 4 2 5 8
# 1 2 4 5 8