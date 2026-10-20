# Cream o lista de numere
v = [5, 2, 8, 1, 3]

# Parcurgem lista de mai multe ori
for i in range(len(v) - 1):

    # Comparam elementele vecine
    # - i ne ajuta sa nu mai verificam elementele deja sortate
    for j in range(len(v) - 1 - i):

        # Daca elementul din stanga este mai mare decat cel din dreapta
        if v[j] > v[j + 1]:

            # Interschimbam cele doua elemente
            aux = v[j]
            v[j] = v[j + 1]
            v[j + 1] = aux

# Afisam lista sortata crescator
print("Lista sortata:", v)
