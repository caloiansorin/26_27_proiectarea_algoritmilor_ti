#include <iostream>
using namespace std;

int main()
{
    int v[100], n, aux;

    cout << "Introdu numarul de elemente: ";
    cin >> n;

    cout << "Introdu elementele vectorului: ";
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }

    for (int i = 0; i < n - 1; i++)
    {
        int pozmin = i;

        for (int j = i + 1; j < n; j++)
        {
            if (v[j] < v[pozmin])
            {
                pozmin = j;
            }
        }

        if (pozmin != i)
        {
            aux = v[i];
            v[i] = v[pozmin];
            v[pozmin] = aux;
        }
    }

    cout << "Vectorul sortat este: ";
    for (int i = 0; i < n; i++)
    {
        cout << v[i] << " ";
    }

    return 0;
}