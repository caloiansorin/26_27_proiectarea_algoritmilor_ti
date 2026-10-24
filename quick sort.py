def quick_sort(arr):
    # Cazul de bază: lista are 0 sau 1 element, deci este deja sortată
    if len(arr) <= 1:
        return arr
    
    # Alegem pivotul (aici luăm elementul din mijloc)
    pivot = arr[len(arr) // 2]
    
    # Împărțim lista în trei sub-liste
    stanga = [x for x in arr if x < pivot]
    mijloc = [x for x in arr if x == pivot]
    dreapta = [x for x in arr if x > pivot]
    
    # Sortăm recursiv stânga și dreapta, apoi le combinăm
    return quick_sort(stanga) + mijloc + quick_sort(dreapta)

# Exemplu de utilizare:
numere = [10, 7, 8, 9, 1, 5]
print("Lista inițială:", numere)

numere_sortate = quick_sort(numere)
print("Lista sortată:", numere_sortate)