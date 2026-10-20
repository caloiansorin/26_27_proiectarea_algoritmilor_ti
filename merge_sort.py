"""
Algoritm: Merge Sort (Sortare prin interclasare)
Descriere: Algoritm de tip Divide et Impera. Împarte recursiv lista în jumătăți
           până ajunge la liste de lungime 1, apoi le combină (interclasează) în ordine.
Complexitate Timp: O(n log n) în toate cazurile.
Complexitate Spațiu: O(n) - necesită memorie suplimentară pentru subliste.
"""

def merge_sort(arr):
    # Pasul 1: Cazul de bază pentru recursivitate (o listă cu un singur element este deja sortată)
    if len(arr) > 1:
        mid = len(arr) // 2  # Găsim mijlocul listei
        
        # Pasul 2: Împărțim lista în două jumătăți (Divide)
        L = arr[:mid]  # Jumătatea stângă
        R = arr[mid:]  # Jumătatea dreaptă

        # Aplicăm recursiv Merge Sort pe fiecare jumătate
        merge_sort(L)
        merge_sort(R)

        # Pasul 3: Interclasarea celor două jumătăți sortate (Impera / Combine)
        i = j = k = 0

        # Comparăm elementele din cele două jumătăți și le adăugăm în ordinea corectă
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copiem elementele rămase din jumătatea stângă (dacă există)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copiem elementele rămase din jumătatea dreaptă (dacă există)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
    return arr


# Bloc de testare
if __name__ == "__main__":
    date_test = [38, 27, 43, 3, 9, 82, 10]
    print("Lista inițială:", date_test)
    rezultat = merge_sort(date_test.copy())
    print("Lista sortată (Merge Sort):", rezultat)