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

        for (int j = 0; j < n - i - 1; j++)
        {

            if (v[j] > v[j + 1])
            {

                aux = v[j];

                v[j] = v[j + 1];

                v[j + 1] = aux;
            }
        }
    }

    cout << "Vectorul sortat este: ";

    for (int i = 0; i < n; i++)
    {

        cout << v[i] << " ";
    }

    return 0;
}