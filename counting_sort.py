def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)


    for num in arr:
        count[num - min_val] += 1

 
    for i in range(1, len(count)):
        count[i] += count[i - 1]


    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output


if __name__ == "__main__":
    date_test = [4, 2, 2, 8, 3, 3, 1]
    print("Lista inițială:", date_test)
    
    lista_sortata = counting_sort(date_test)
    print("Lista sortată: ", lista_sortata)
