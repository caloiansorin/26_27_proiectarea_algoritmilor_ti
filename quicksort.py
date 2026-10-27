def partitionare(arr, low, high):
    """
    Schema de partiționare Lomuto.
    Alege ultimul element ca pivot, îl plasează pe poziția sa corectă
    și mută toate elementele mai mici la stânga, iar cele mai mari la dreapta.
    """
    pivot = arr[high]  # Se alege ca pivot ultimul element din interval
    i = low - 1        # Indicele ultimului element mai mic decât pivotul

    for j in range(low, high):
        # Dacă elementul curent arr[j] este mai mic sau egal cu pivotul
        if arr[j] <= pivot:
            i += 1
            # Interschimbăm elementul curent cu cel de pe indicele i
            arr[i], arr[j] = arr[j], arr[i]

    # Plasăm pivotul pe poziția sa finală și corectă (i + 1)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Returnăm indicele unde a fost plasat pivotul
    return i + 1


def quicksort(arr, low, high):
    """
    Funcția recursivă Quick Sort pe bază de indici:
    - arr: lista de sortat
    - low: indicele de început (stânga)
    - high: indicele de sfârșit (dreapta)
    """
    if low < high:
        # pi este indicele pivotului după partiționare (arr[pi] e la locul lui)
        pi = partitionare(arr, low, high)

        # Apel recursiv pentru sub-tabloul din stânga pivotului
        quicksort(arr, low, pi - 1)

        # Apel recursiv pentru sub-tabloul din dreapta pivotului
        quicksort(arr, pi + 1, high)


# Exemplu de rulare și testare
if __name__ == "__main__":
    vector = [10, 7, 8, 9, 1, 5]
    n = len(vector)

    print("Vector inițial:", vector)
    
    # Apelăm quicksort cu indicele 0 (low) și n-1 (high)
    quicksort(vector, 0, n - 1)
    
    print("Vector final sortat:", vector)