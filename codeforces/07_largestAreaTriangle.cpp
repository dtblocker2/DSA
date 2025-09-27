#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

double largestTriangleArea(vector<vector<int>>& points)
{
    double curArea, maxArea = 0;
    int n = points.size();

    for (int i=0; i<n; i++)
    {
        int x1 = points[i][0];
        int y1 = points[i][1];
        for (int j=0; j<n; j++)
        {
            if (j==i)
            {
                continue;
            };
            int x2 = points[j][0];
            int y2 = points[j][1];
            for (int k=0; k<n; k++)
            {
                if ((j==k) || (k==i))
                {
                    continue;
                };
                int x3 = points[k][0];
                int y3 = points[k][1];
                curArea = 0.5 * abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2));
                if (curArea > maxArea){
                    maxArea = curArea;
                };
            };
        };
    };
    return maxArea;
};

int main()
{
    vector<vector<int>> input= {{1,0},{0,0},{1,2}};
    cout<<largestTriangleArea(input)<<endl;
    return 0;
};