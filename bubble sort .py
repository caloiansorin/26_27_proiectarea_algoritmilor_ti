def bubble_sort(arr):
    n = len(arr)
    # Parcurgem toate elementele listei
    for i in range(n):
        swapped = False
        
        # Ultimele i elemente sunt deja sortate
        for j in range(0, n - i - 1):
            # Comparăm elementele adiacente
            if arr[j] > arr[j + 1]:
                # Schimbăm elementele dacă nu sunt în ordine
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # Dacă nu s-a făcut nicio schimbare, lista este deja sortată
        if not swapped:
            break
            
    return arr