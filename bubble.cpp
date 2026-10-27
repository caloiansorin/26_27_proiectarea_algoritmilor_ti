#include <iostream>
using namespace std;
void bubbleiteration(int v[], int n)
{
    int c;
    for (int i=0;i<n-1;i++)
        if (v[i]>v[i+1])
            {
                v[i]=c;
                v[i]=v[i+1];
                v[i+1]=c;
            }
}
bool sortcheck(int v[], int n)
{
    for (int i=0;i<n-1;i++)
    {
        if (v[i]>v[i+1])
            return false;
    }
    return true;
}
int main()
{
    int v[50], n;
    cout << "Introd nr. elemente\n";
    cin >> n;
    cout << "Introd elementele\n";
    for (int i=0;i<n;i++)
        cin >> v[i];
    while (!(sortcheck(v,n)))
        bubbleiteration(v, n);
    cout << "Vectorul sortat:\n";
    for (int i=0; i<n;i++)
        cout << v[i] << " ";
}
