def radix_sort(lista):
    pozitie = 1   # 1 = unitati, 10 = zeci, 100 = sute, ...
    pas = 1
    print("Lista initiala:", lista)
    while pozitie <= max(lista):
        # sortam toata lista dupa cifra curenta;
        # la cifre egale, sorted() pastreaza ordinea aparitiei
        lista = sorted(lista, key=lambda numar: (numar // pozitie) % 10) # lambda este o scurtătură pentru a scrie o funcție mică, fără nume
                                                                         # numar = 457 cu pozitie = 1: 457 // 1 = 457, apoi 457 % 10 = 7, 
                                                                                     # cu pozitie = 10: 457 // 10 = 45, apoi 45 % 10 = 5, 
                                                                                     # cu pozitie = 100: 457 // 100 = 4, apoi 4 % 10 = 4 
        print("Pasul", pas, ":", lista)
        pozitie *= 10
        pas += 1
    return lista

print("Rezultat:", radix_sort([329, 457, 657, 839, 436, 720, 355]))

"""
Initial   Pasul 1   Pasul 2   Pasul 3
          (unități) (zeci)    (sute)
329       72[0]     7[2]0     [3]29
457       35[5]     3[2]9     [3]55
657       43[6]     4[3]6     [4]36
839       45[7]     8[3]9     [4]57
436       65[7]     3[5]5     [6]57
720       32[9]     4[5]7     [7]20
355       83[9]     6[5]7     [8]39
"""