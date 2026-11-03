#include <iostream>
using namespace std;
void selectionsort (int v[], int n)
{
    int poz, c;
    for (int i=0;i<n-1;i++)
    {
        poz=i;
        for (int j=i+1;j<n;j++)
        {
            if (v[j]<=v[poz])
                poz=j;
        }
        c=v[i];
        v[i]=v[poz];
        v[poz]=c;
    }
}
int main()
{
    int v[50], n;
    cout << "Introd nr. elemente\n";
    cin >> n;
    cout << "Introd elementele\n";
    for (int i=0;i<n;i++)
        cin >> v[i];
    selectionsort(v, n);
    cout << "Vectorul sortat:\n";
    for (int i=0; i<n;i++)
        cout << v[i] << " ";
}
