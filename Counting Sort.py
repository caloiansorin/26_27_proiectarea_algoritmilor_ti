def counting_sort(arr):
    if not arr:
        return arr

    # Găsim valoarea maximă și minimă din listă
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Creăm vectorul de frecvență și cel de ieșire
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Calculăm frecvența fiecărui element
    for num in arr:
        count[num - min_val] += 1

    # Calculăm pozițiile finale ale elementelor
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Construim lista sortată
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1

    # Copiem elementele sortate în lista originală
    for i in range(len(arr)):
        arr[i] = output[i]

    return arr

