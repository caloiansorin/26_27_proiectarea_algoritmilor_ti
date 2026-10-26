numere = [98, 32, 1, 19, 6, 65, 4]
for k in range(1, len(numere)):
    i = k
    while i > 0 and numere[i - 1] > numere[i]:
        numere[i - 1], numere[i] = numere[i], numere[i - 1]
        i = i - 1
print(numere)