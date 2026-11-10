#include <iostream>
using namespace std;
void copy(int v[], int x[], int m, int n)
{
    for (int i=m;i<=n;i++)
        v[i]=x[i];
}
void qsort(int v[], int x[], int m, int n)
{
    if ((n-m)<=0)
        return;
    int a=m, b=n;
    for (int i=m;i<n;i++)
    {
        if (v[i]<=v[n])
        {
            x[a]=v[i];
            a++;
        }
        else
        {
            x[b]=v[i];
            b--;
        }
    }
    x[a]=v[n];
    qsort(x, v, 0, a-1);
    copy (v, x, m, n);
    qsort(x, v, a+1, n);
    copy (v, x, m, n);
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
    qsort(v, x, 0, n-1);
    cout << "Vectorul sortat:\n";
    for (int i=0; i<n;i++)
        cout << v[i] << " ";
}
