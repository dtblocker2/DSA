#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin>>t;
    vector<string> outputArr;

    for (int pm=0; pm<t; pm++)
    {
        
        int n,t,z2=0;
        vector<int> grarr;
    
        cin>>n;
        for (int i=0; i<n; i++)
        {
            int p;
            cin>>p;
            grarr.push_back(p);
        };
    
        for (int x=0; x<grarr.size();x++)
        {
            int z;
            // cout<<x<<endl;
            for (int y=0; y<grarr.size(); y++)
            {
                if((grarr[x]==grarr[y]) && (y!=x))
                {
                    z = grarr[y];
                    break;
                };
            };
    
            if(grarr[x]==z)
            {
                // cout<<x<<" "<<z<<endl;
                // cout<<"YES"<<endl;
                outputArr.push_back("YES");
                z2=1;
                break;
            }
        };
    
        if (z2==0)
        {
            outputArr.push_back("NO");
            // cout<<"NO"<<endl;
        };
    };

    for (string x:outputArr)
    {
        cout<<x<<endl;
    };
    return 0;
};