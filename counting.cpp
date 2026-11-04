#include <iostream>
using namespace std;

void countingSort(int v[], int n)
{
    int maxim = v[0];

    // Determinam valoarea maxima
    for (int i = 1; i < n; i++)
    {
        if (v[i] > maxim)
            maxim = v[i];
    }

    // Cream vectorul de frecventa
    int *frecventa = new int[maxim + 1]();

    // Calculam frecventa fiecarei valori
    for (int i = 0; i < n; i++)
    {
        frecventa[v[i]]++;
    }

    // Reconstruim vectorul sortat
    int k = 0;

    for (int i = 0; i <= maxim; i++)
    {
        while (frecventa[i] > 0)
        {
            v[k] = i;
            k++;
            frecventa[i]--;
        }
    }

    delete[] frecventa;
}

int main()
{
    int v[] = {4, 2, 2, 8, 3, 3, 1};
    int n = 7;

    countingSort(v, n);

    cout << "Vectorul sortat este: ";

    for (int i = 0; i < n; i++)
        cout << v[i] << " ";

    return 0;
}