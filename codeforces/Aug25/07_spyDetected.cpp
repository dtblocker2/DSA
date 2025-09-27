#include <iostream>
using namespace std;

namespace naiveSolution
{
    void solution()
    {
        int n;
        cin>>n;
        int a[n];
        int sum = 0;
        for (int i=0; i<n; i++)
        {
            cin>>a[i];
        };

        for (int i=0; i<n; i++)
        {
            sum += a[i];

            if ((sum != a[0]*(i+1)) && (a[i] != a[i+1]))
            {
                cout<<a[i]<<endl;
                break;
            };
            
            if ((sum != a[0]*(i+1)) && (a[i] == a[i+1]))
            {
                cout<<a[i-1]<<endl;
                break;
            };
        };


        /* for (int x:a)
        {
            sum += x;

        }; */
    };

};

int main()
{
    int t;
    cin>>t;

    while (t--)
    {
        naiveSolution::solution();
    };

    return 0;
};