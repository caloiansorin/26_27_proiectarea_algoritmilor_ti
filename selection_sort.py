"""
Algoritm: Selection Sort (Sortare prin selecție)
Descriere: Împarte lista în două părți: sublista sortată și sublista nesortată.
           La fiecare pas, caută elementul minim din sublista nesortată și îl mută la finalul sublistei sortate.
Complexitate Timp: O(n^2) în toate cazurile.
Complexitate Spațiu: O(1) - sortare in-place.
"""

def selection_sort(arr):
    n = len(arr)
    
    # Pasul 1: Trecem prin toate elementele tabloului
    for i in range(n):
        # Presupunem că primul element nesortat este cel mai mic
        min_idx = i
        
        # Pasul 2: Căutăm minimul în restul tabloului nesortat
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Pasul 3: Interschimbăm elementul minim găsit cu primul element nesortat
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr


# Bloc de testare
if __name__ == "__main__":
    date_test = [64, 25, 12, 22, 11]
    print("Lista inițială:", date_test)
    rezultat = selection_sort(date_test.copy())
    print("Lista sortată (Selection Sort):", rezultat)