def counting_sort(arr):
    maxim = max(arr)

    count = [0] * (maxim + 1)

    for num in arr:
        count[num] += 1

    rezultat = []

    for i in range(len(count)):
        for j in range(count[i]):
            rezultat.append(i)

    return rezultat


# Exemplu de utilizare
lista = [4, 2, 2, 8, 3, 3, 1]

print("Lista initiala:", lista)
print("Lista sortata:", counting_sort(lista))