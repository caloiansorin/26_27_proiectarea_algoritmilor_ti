# Merge Sort, Insertion Sort, Bubble Sort, Selection Sort

def bubble_sort(arr):
    a = arr[:]
    n = len(a)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if not swapped:
            break

    return a


def insertion_sort(arr):
    a = arr[:]
    n = len(a)

    for i in range(1, n):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

    return a


def selection_sort(arr):
    a = arr[:]
    n = len(a)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a


def merge_sort(arr):
    a = arr[:]

    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11, 90, 7, 53]

    print("Lista initiala:", arr)
    print("Bubble Sort:", bubble_sort(arr))
    print("Insertion Sort:", insertion_sort(arr))
    print("Selection Sort:", selection_sort(arr))
    print("Merge Sort:", merge_sort(arr))