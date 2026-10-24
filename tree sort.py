class Nod:
    def __init__(self, cheie):
        self.val = cheie
        self.stanga = None
        self.dreapta = None

# Funcție pentru introducerea unui nod nou în BST
def insereaza(radacina, cheie):
    if radacina is None:
        return Nod(cheie)
    
    if cheie < radacina.val:
        radacina.stanga = insereaza(radacina.stanga, cheie)
    else:
        radacina.dreapta = insereaza(radacina.dreapta, cheie)
        
    return radacina

# Parcurgerea în inordine (In-order traversal) extrage elementele sortate
def parcurgere_inordine(radacina, rezolvare):
    if radacina:
        parcurgere_inordine(radacina.stanga, rezolvare)
        rezolvare.append(radacina.val)
        parcurgere_inordine(radacina.dreapta, rezolvare)

def tree_sort(arr):
    if not arr:
        return arr

    radacina = None
    # Construim arborele binar de căutare
    for elem in arr:
        radacina = insereaza(radacina, elem)

    # Salvăm elementele sortate înapoi în listă
    rezolvare = []
    parcurgere_inordine(radacina, rezolvare)
    
    for i in range(len(arr)):
        arr[i] = rezolvare[i]

    return arr

