def heapify(arr, n, i):
    largest = i  # Inițializăm cel mai mare element ca fiind rădăcina
    stanga = 2 * i + 1
    dreapta = 2 * i + 2

    # Verificăm dacă copilul din stânga există și este mai mare decât rădăcina
    if stanga < n and arr[stanga] > arr[largest]:
        largest = stanga

    # Verificăm dacă copilul din dreapta există și este mai mare decât cel mai mare de până acum
    if dreapta < n and arr[dreapta] > arr[largest]:
        largest = dreapta

    # Dacă cel mai mare element nu este rădăcina
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Inversăm

        # Aplicăm recursiv heapify pe subarborele afectat
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construim Max-Heap-ul (reorganizăm lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extragerea elementelor unul câte unul din heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Mutăm rădăcina curentă la sfârșit
        heapify(arr, i, 0)  # Apelăm max heapify pe heap-ul redus

    return arr

