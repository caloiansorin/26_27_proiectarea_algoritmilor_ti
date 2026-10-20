#include <iostream>

using namespace std;

int v[100], aux[100];

void interclasare(int st, int mij, int dr)
{

    int i = st, j = mij + 1, k = st;

    while (i <= mij && j <= dr)
    {

        if (v[i] < v[j])

            aux[k++] = v[i++];

        else

            aux[k++] = v[j++];
    }

    while (i <= mij)

        aux[k++] = v[i++];

    while (j <= dr)

        aux[k++] = v[j++];

    for (i = st; i <= dr; i++)

        v[i] = aux[i];
}

void mergeSort(int st, int dr)
{

    if (st < dr)
    {

        int mij = (st + dr) / 2;

        mergeSort(st, mij);

        mergeSort(mij + 1, dr);

        interclasare(st, mij, dr);
    }
}

int main()
{

    int n;

    cout << "Introdu numarul de elemente: ";

    cin >> n;

    cout << "Introdu elementele vectorului: ";

    for (int i = 0; i < n; i++)

        cin >> v[i];

    mergeSort(0, n - 1);

    cout << "Vectorul sortat este: ";

    for (int i = 0; i < n; i++)

        cout << v[i] << " ";

    return 0;
}