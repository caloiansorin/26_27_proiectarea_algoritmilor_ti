numere = [6, 1, 99, 15, 28]
for tura in range(len(numere)-1):
    for i in range(len(numere)-1):
        if numere[i] > numere[i+1]:
            numere[i], numere[i+1] = numere[i+1], numere[i]
print(numere)