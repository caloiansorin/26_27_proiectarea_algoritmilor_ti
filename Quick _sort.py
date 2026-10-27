numere = [2, 9, 7, 4, 3, 1, 10]
pivot = numere[0]
mai_mici = []
mai_mari = []

for numar in numere[1:]:
    if numar < pivot:
        mai_mici.append(numar)
    else:
        mai_mari.append(numar)
print("Pivot:", pivot)
print("Mai mici:", mai_mici)
print("Mai mari:", mai_mari)