def selection_sort(v):
    n = len(v)

    for i in range(n - 1):
        poz_min = i

        for j in range(i + 1, n):
            if v[j] < v[poz_min]:
                poz_min = j

        v[i], v[poz_min] = v[poz_min], v[i]

    return v


v = [5, 2, 8, 1, 9, 3]

print("Vectorul sortat este:", selection_sort(v))