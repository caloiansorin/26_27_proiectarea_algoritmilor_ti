#include <iostream>
using namespace std;

int maxim(int v[], int n)
{
    int m = v[0];

    for (int i = 1; i < n; i++)
        if (v[i] > m)
            m = v[i];

    return m;
}

void countingSort(int v[], int n, int exp)
{
    int output[1000];
    int count[10] = {0};

    for (int i = 0; i < n; i++)
        count[(v[i] / exp) % 10]++;

    for (int i = 1; i < 10; i++)
        count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--)
    {
        int cifra = (v[i] / exp) % 10;
        output[count[cifra] - 1] = v[i];
        count[cifra]--;
    }

    for (int i = 0; i < n; i++)
        v[i] = output[i];
}

void radixSort(int v[], int n)
{
    int m = maxim(v, n);

    for (int exp = 1; m / exp > 0; exp *= 10)
        countingSort(v, n, exp);
}

int main()
{
    int n, v[1000];

    cout << "Introduceti numarul de elemente: ";
    cin >> n;

    cout << "Introduceti elementele vectorului: ";

    for (int i = 0; i < n; i++)
        cin >> v[i];

    radixSort(v, n);

    cout << "Vectorul sortat este: ";

    for (int i = 0; i < n; i++)
        cout << v[i] << " ";

    return 0;
}