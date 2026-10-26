numere = [12, 3, 78, 23, 1, 100, 5]
for loc in range(len(numere) - 1):
    poz_min = loc
    for i in range(loc + 1, len(numere)):
        if numere[i] < numere[poz_min]:
            poz_min = i
    numere[loc], numere[poz_min] = numere[poz_min], numere[loc]
print(numere)