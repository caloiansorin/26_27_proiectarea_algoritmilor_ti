def counting_sort_pentru_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Calculăm frecvența cifrelor de pe poziția curentă (exp)
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Schimbăm count[i] astfel încât să conțină poziția reală
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construim lista de ieșire
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copiem elementele în lista originală
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr

    # Găsim numărul maxim pentru a ști numărul de cifre
    max_val = max(arr)

    # Aplicăm Counting Sort pentru fiecare cifră (1, 10, 100, ...)
    exp = 1
    while max_val // exp > 0:
        counting_sort_pentru_radix(arr, exp)
        exp *= 10

    return arr

