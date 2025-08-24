#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    // test cases t
    int t,n,m;
    string a,b,c,output;
    
    int p=0;
    cin >> t;
    string outputArr[t];

    while (p<t)
    {
        /* logic here */
        cin>>n>>a>>m>>b>>c;
        output = a;
        for (int i=0; i<c.length(); i++)
        {
            if (c[i]=='D')
            {
                output = output + b[i];
            }
            else
            {
                output = b[i] + output;
            };
        };

        outputArr[p] = output;
        p++;
    };
    
    for (string x:outputArr)
    {
        cout<<x<<endl;
    };

    return 0;
};
