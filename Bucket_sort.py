def bucket_sort(lista):
    k = 10                       
    maxim = max(lista)   # găsește cel mai mare număr din listă
    lungime = maxim // k + 1       # calculeaza cate valori acopera o galeata; 839 // 10 + 1 = 83 + 1 = 84; deci galeata 0 ține valorile 0-83, galeata 1 ține 84-167...

    galeti = [[] for _ in range(k)]
    for x in lista:
        galeti[x // lungime].append(x)    # fiecare număr x este pus în galeata lui

    rezultat = []
    for galeata in galeti:
       rezultat += sorted(galeata)
    return rezultat

print(bucket_sort([329, 457, 657, 839, 436, 720, 355]))
print(bucket_sort([5, 12, 7, 1000000, 33, 0, 999999]))




""" Pentru o lista cu toate numerele de ordinul sutelor
def bucket_sort(lista):
    galeti = [[] for _ in range(10)]
    for numar in lista:
        galeti[numar // 100].append(numar)
    rezultat = []
    for galeata in galeti:
        rezultat += sorted(galeata)
    return rezultat

print(bucket_sort([329, 457, 657, 839, 436, 720, 355]))
"""