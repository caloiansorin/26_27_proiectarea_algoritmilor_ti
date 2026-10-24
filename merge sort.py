def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        stanga = arr[:mid]
        dreapta = arr[mid:]

        # Apelăm recursiv pentru fiecare jumătate
        merge_sort(stanga)
        merge_sort(dreapta)

        i = j = k = 0

        # Interclasarea celor două jumătăți
        while i < len(stanga) and j < len(dreapta):
            if stanga[i] < dreapta[j]:
                arr[k] = stanga[i]
                i += 1
            else:
                arr[k] = dreapta[j]
                j += 1
            k += 1

        # Verificăm dacă au mai rămas elemente în stânga
        while i < len(stanga):
            arr[k] = stanga[i]
            i += 1
            k += 1

        # Verificăm dacă au mai rămas elemente în dreapta
        while j < len(dreapta):
            arr[k] = dreapta[j]
            j += 1
            k += 1

    return arr

