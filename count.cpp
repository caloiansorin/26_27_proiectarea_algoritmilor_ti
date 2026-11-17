#include <iostream>
using namespace std;
void countsort(int v[], int n, int x[])
{
    int count[50], i;
    for (i=0;i<50;i++)
        count[i]=0;
    for (i=0;i<n;i++)
        count[v[i]]++;
    for (i=1;i<50;i++)
        count[i]+=count[i-1];
    for (i=0;i<n;i++)
    {
        x[count[v[i]]-1]=v[i];
        count[v[i]]--;
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
    int x[50];
    countsort(v, n, x);
    cout << "Vectorul sortat:\n";
    for (int i=0; i<n;i++)
        cout << x[i] << " ";
}
