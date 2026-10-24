def insertion_sort(arr):
    # Parcurgem lista de la al doilea element până la final
    for i in range(1, len(arr)):
        cheie = arr[i]
        j = i - 1
        
        # Mutăm elementele din arr[0..i-1] care sunt mai mari decât cheia
        # cu o poziție mai la dreapta
        while j >= 0 and cheie < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = cheie

    return arr

