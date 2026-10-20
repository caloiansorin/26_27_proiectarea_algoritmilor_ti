def bubble_sort(v):
    n = len(v)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]

    return v


v = [5, 2, 8, 1, 9, 3]

print("Vectorul sortat este:", bubble_sort(v))