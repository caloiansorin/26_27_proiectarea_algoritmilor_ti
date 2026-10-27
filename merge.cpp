#include <iostream>
using namespace std;
void merge(int v[50], int beg, int mid, int end, int x[50])
{
    int i=beg;
    int j=mid;
    for (int k=beg;k<end;++k)
    {
    if ((i<mid)&&((j>=end)||(v[i]<=v[j])))
    {
        x[k]=v[i];
        i++;
    }
    else
    {
        x[k]=v[j];
        j++;
    }
}
}
void split(int v[50], int beg, int end, int x[50])
{
    if ((end-beg)<=1)
        return;
    int mid = (beg+end)/2;
    split (x, beg, mid, v);
    split (x, mid, end, v);
    merge (x, beg, mid, end, v);
}
int main()
{
    int v[50], x[50], n;
    cout << "Introd nr. elemente\n";
    cin >> n;
    cout << "Introd elementele\n";
    for (int i=0;i<n;i++)
        cin >> v[i];
    for (int i=0;i<n;i++)
        x[i]=v[i];
    split(v, 0, n, x);
    cout << "Vectorul sortat:\n";
    for (int i=0; i<n;i++)
        cout << v[i] << " ";
}
