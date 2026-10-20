# Proiectarea algoritmilor – Algoritmi de sortare

Acest repository conține implementări în **Python** ale principalilor algoritmi de sortare, utilizate în cadrul disciplinei **Proiectarea algoritmilor**.

## Algoritmi studiați

1. **Merge Sort** – sortare prin interclasare.
2. **Quick Sort** – sortare rapidă prin partiționare.
3. **Insertion Sort** – sortare prin inserție.
4. **Selection Sort** – sortare prin selecție.
5. **Counting Sort** – sortare prin numărare.
6. **Bucket Sort** – sortare prin distribuire în compartimente.
7. **Radix Sort** – sortare pe baza pozițiilor cifrelor.
8. **Heap Sort** – sortare utilizând structura de date heap.
9. **Tree Sort** – sortare prin arbori binari de căutare.

## Complexitatea algoritmilor

| Algoritm | Caz mediu | Caz nefavorabil |
|---|---|---|
| Merge Sort | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n²) |
| Insertion Sort | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) |
| Counting Sort | O(n + k) | O(n + k) |
| Bucket Sort | O(n + k) | O(n²) |
| Radix Sort | O(d(n + k)) | O(d(n + k)) |
| Heap Sort | O(n log n) | O(n log n) |
| Tree Sort (BST neechilibrat) | O(n log n) | O(n²) |

Complexitățile pentru Bucket Sort și Radix Sort depind de implementare și de distribuția datelor.


## Încărcarea lucrării pe GitHub

Înlocuiește `Nume-Prenume` cu datele tale.

### 1. Descarcă repository-ul și intră în folder

```bash
git clone https://github.com/caloiansorin/26_27_proiectarea_algoritmilor_ti
cd REPO
```

### 2. Treci pe branch-ul tău

Dacă branch-ul există deja:

```bash
git fetch origin
git switch Nume-Prenume
```

Dacă trebuie să creezi un branch nou:

```bash
git switch -c Nume-Prenume
```

### 3. Adaugă și trimite modificările

După ce ai salvat fișierele lucrării, rulează:

```bash
git add .
git commit -m "Am adăugat rezolvarea"
git push -u origin Nume-Prenume
```

**Atenție:** lucrează pe branch-ul tău. Nu încărca modificările pe `main`.

La următoarele încărcări, repetă doar comenzile de la pasul 3.