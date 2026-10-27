def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        p = partition(arr, low, high)
        quick_sort_inplace(arr, low, p)        
        quick_sort_inplace(arr, p + 1, high)


def partition(arr, low, high):
    pivot = arr[(low + high) // 2]   
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:      
            i += 1

        j -= 1
        while arr[j] > pivot:        
            j -= 1

        if i >= j:                 
            return j

        arr[i], arr[j] = arr[j], arr[i]


numere = [2, 10, 7, 26, 20, 8, 29]
quick_sort_inplace(numere)
print(numere)