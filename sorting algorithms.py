def quick_sort(arr):
    """Sorts a list using the Quick Sort algorithm.
    
    Time complexity:
        - Best case: O(n log n)
        - Average case: O(n log n)
        - Worst case: O(n^2)
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Exemplu de utilizare
if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Lista initiala:", numbers)
    print("Lista sortata (Quick Sort):", quick_sort(numbers))
