"""
Algoritm: Bubble Sort (Sortare prin metoda bulelor)
Descriere: Parcurge repetat lista, comparând elementele adiacente și
           interschimbându-le dacă sunt în ordine greșită.
Complexitate Timp: O(n^2) în cazul defavorabil, O(n) în cazul favorabil.
Complexitate Spațiu: O(1) - sortare în memorie locală (in-place).
"""

def bubble_sort(arr):
    n = len(arr)
    
    # Pasul 1: Parcurgem toate elementele tabloului
    for i in range(n):
        # Variabilă de optimizare pentru a verifica dacă s-au făcut interschimbări
        swapped = False
        
        # Pasul 2: Ultimele i elemente sunt deja la locul lor corect
        for j in range(0, n - i - 1):
            # Pasul 3: Comparăm elementele adiacente
            if arr[j] > arr[j + 1]:
                # Interschimbăm dacă elementul curent este mai mare decât următorul
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Pasul 4: Dacă nu s-a făcut nicio interschimbare, lista este deja sortată
        if not swapped:
            break
            
    return arr


# Bloc de testare
if __name__ == "__main__":
    date_test = [64, 34, 25, 12, 22, 11, 90]
    print("Lista inițială:", date_test)
    rezultat = bubble_sort(date_test.copy())
    print("Lista sortată (Bubble Sort):", rezultat)