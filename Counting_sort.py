def counting_sort(arr):
    if not arr:
        return []
    
    max_val = max(arr)
    
    # se creeaza lista de lungime max_val + 1, plina cu zero
    count = [0] * (max_val + 1)
    
    # se numara de cate ori apare fiecare nr
    for num in arr:
        count[num] += 1
        
    # este reconstruit sirul sortat
    rezultat = []
    for i in range(len(count)):
        rezultat.extend([i] * count[i])  # se adauga numarul i de count[i] ori
        
    return rezultat

numere = [4, 2, 2, 8, 3, 3, 1, 5]
print("Șirul inițial:", numere)

print("Șirul sortat: ", counting_sort(numere))