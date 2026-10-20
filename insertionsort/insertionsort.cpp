#include <iostream>
using namespace std;

int main()
{
    int v[50], n;
    cout << "Introd nr. elemente\n";
    cin >> n;
    cout << "Introd elementele\n";
    for (int i=0;i<n;i++)
        cin >> v[i];
    int c;
    for (int i=1;i<n;i++)
    {
        for (int j=i;((j>0)&&(v[j-1]>v[j]));j--)
        {
            c=v[j];
            v[j]=v[j-1];
            v[j-1]=c;
        }
    }
    cout << "Vectorul sortat:\n";
    for (int i=0; i<n;i++)
        cout << v[i] << " ";
}
