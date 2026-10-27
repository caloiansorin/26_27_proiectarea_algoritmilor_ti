#include <iostream>
using namespace std;

void quickSort(int v[], int st, int dr)
{
    int i = st, j = dr;
    int pivot = v[(st + dr) / 2];

    while (i <= j)
    {
        while (v[i] < pivot)
            i++;

        while (v[j] > pivot)
            j--;

        if (i <= j)
        {
            swap(v[i], v[j]);
            i++;
            j--;
        }
    }

    if (st < j)
        quickSort(v, st, j);

    if (i < dr)
        quickSort(v, i, dr);
}

int main()
{
    int n, v[100];

    cout << "Introduceti numarul de elemente: ";
    cin >> n;

    cout << "Introduceti elementele vectorului: ";
    for (int i = 0; i < n; i++)
        cin >> v[i];

    quickSort(v, 0, n - 1);

    cout << "Vectorul sortat crescator este: ";
    for (int i = 0; i < n; i++)
        cout << v[i] << " ";

    return 0;
}