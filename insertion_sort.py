"""
Algoritm: Insertion Sort (Sortare prin inserție)
Descriere: Construiește lista sortată câte un element pe rând, inserând fiecare
           element nou pe poziția sa corectă relativ la elementele deja sortate.
Complexitate Timp: O(n^2) în cazul defavorabil, O(n) în cazul favorabil.
Complexitate Spațiu: O(1) - sortare in-place.
"""

def insertion_sort(arr):
    # Pasul 1: Începem de la al doilea element (indexul 1)
    for i in range(1, len(arr)):
        key = arr[i]  # Elementul pe care vrem să-l inserăm la locul potrivit
        j = i - 1
        
        # Pasul 2: Mutăm elementele mai mari decât 'key' cu o poziție la dreapta
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Pasul 3: Plasăm 'key' la poziția sa corectă
        arr[j + 1] = key
        
    return arr


# Bloc de testare
if __name__ == "__main__":
    date_test = [12, 11, 13, 5, 6]
    print("Lista inițială:", date_test)
    rezultat = insertion_sort(date_test.copy())
    print("Lista sortată (Insertion Sort):", rezultat)