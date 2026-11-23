def intoarce(lista, k):
    # rastoarna primele k elemente, schimband capetele intre ele
    sus = 0
    jos = k - 1
    while sus < jos:
        lista[sus], lista[jos] = lista[jos], lista[sus]
        sus += 1
        jos -= 1

def flipping_sort(lista):
    print("Lista initiala:", lista)
    for dimensiune in range(len(lista), 1, -1):   # range(început, sfârșit, pas)
        # cautam pozitia celui mai mare numar din partea nesortata
        poz_max = 0
        for i in range(dimensiune):
            if lista[i] > lista[poz_max]:
                poz_max = i

        intoarce(lista, poz_max + 1)   # il aducem sus
        intoarce(lista, dimensiune)    # il trimitem jos, la locul lui
    return lista

print("Lista sortata: ",flipping_sort([329, 457, 657, 839, 436, 720, 355]))

# Sortarea prin răsturnare este cunoscută și ca „pancake sort”
# Singura operație permisă este să răstorni primele k elemente ale listei, ca atunci când întorci cu o paleta o stivă de clătite