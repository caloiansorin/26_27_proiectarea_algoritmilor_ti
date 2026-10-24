def insertion_sort_pentru_buckets(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Determinăm valoarea minimă și maximă pentru a calcula intervalele
    min_val, max_val = min(arr), max(arr)
    
    # Numărul de bucket-uri (compartimente)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    
    # Distribuim elementele în bucket-uri
    range_val = (max_val - min_val) / bucket_count
    if range_val == 0:  # Toate elementele sunt egale
        return arr

    for num in arr:
        index = int((num - min_val) / range_val)
        if index >= bucket_count:  # Tratăm cazul limitei maxime
            index = bucket_count - 1
        buckets[index].append(num)

    # Sortăm fiecare bucket și îmbinăm rezultatele
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(insertion_sort_pentru_buckets(bucket))

    # Copiem elementele în lista originală
    for i in range(len(arr)):
        arr[i] = sorted_arr[i]

    return arr

