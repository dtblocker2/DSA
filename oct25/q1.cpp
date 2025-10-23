/* El fucho */

#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while (t--)
    {
        int n,m=0, output=0;
        cin >> n;

        while ((n/2) || (m/2))
        {
            output += n/2;
            m = m+n/2;
            output += m/2;
            n = n%2==1 ? n/2 + 1: n/2;
            m = m%2==1 ? m/2 +1: m/2;
        };
        cout<<(output+1)<<endl;
    };

    return 0;
};