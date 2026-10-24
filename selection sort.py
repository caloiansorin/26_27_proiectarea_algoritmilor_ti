def selection_sort(arr):
    n = len(arr)
    
    # Parcurgem fiecare element al listei
    for i in range(n):
        # Presupunem că primul element nesortat este cel mai mic
        min_idx = i
        
        # Căutăm cel mai mic element din restul listei
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Schimbăm elementul minim găsit cu primul element nesortat
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr