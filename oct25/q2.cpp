#include <iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;

    while(t--)
    {
        int n;
        cin>>n;
        int a;
        cin>>a;
        n -= 1;
        int max=a;
        while(n--)
        {
            cin>>a;

            if (max<a)
            {
                max = a;
            };
        };
        cout<<max<<endl;
    };
    return 0;
};