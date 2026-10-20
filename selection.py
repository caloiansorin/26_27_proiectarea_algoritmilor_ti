def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Presupunem că elementul curent este cel mai mic
        min_idx = i
        # Căutăm un element și mai mic în restul listei
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Dacă am găsit un element mai mic, le interschimbăm
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Exemplu de utilizare:
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)  # Output: [11, 12, 22, 25, 64]