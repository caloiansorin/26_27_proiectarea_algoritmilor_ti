def insertion_sort(v):
    n = len(v)

    for i in range(1, n):
        x = v[i]
        j = i - 1

        while j >= 0 and v[j] > x:
            v[j + 1] = v[j]
            j -= 1

        v[j + 1] = x

    return v


v = [5, 2, 8, 1, 9, 3]

print("Vectorul sortat este:", insertion_sort(v))