def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]

    insertionSort(arr)
    print(*arr)
