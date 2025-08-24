#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool descend(long long int a, long long int b)
{
    return a>b;
};

int main()
{
    long int t;
    vector<long long int> outputArr;
    cin>>t;

    for (long int p=0; p<t;p++)
    {
        long long unsigned int n,z, sum=0;
        vector<long long unsigned int> grump;

        cin>>n;
        z=n/2;
        for (int i=0; i<n; i++)
        {
            int p;
            cin>>p;
            grump.push_back(p);
        };

        sort(grump.begin(), grump.end(),descend);

        for (int i=0; i<=z; i++)
        {
            if (2*i < n)
            {
                sum += grump[2*i];
            };
        };

    // cout<<sum<<endl;
        outputArr.push_back(sum);
    };

    for (long long int x:outputArr)
    {
        cout<<x<<endl;
    };

    return 0;
}