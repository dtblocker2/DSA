// #naive solution using 3 iteration 
/* 
complexity ==> O(n^3)
*/
#include <iostream>
#include <vector>
using namespace std;

/* int threeSumClosest(vector<int>& nums, int target) {
    int sumClosest, sumTemp;
        for (int i=0; i < nums.size(); i++) {
            for (int j=0; j < nums.size(); j++) {
                if (i == j) {
                    continue;
                };

                for (int k=0; k < nums.size(); k++) {
                    if (k ==j || k==i) {
                        continue;
                    };

                    sumTemp = nums[i] + nums[j] + nums[k];

                    if (i==0 && j==1 && k==2) {
                        sumClosest = sumTemp;
                    };

                    if (abs(sumTemp - target) < abs(sumClosest - target)) {
                        sumClosest = sumTemp;
                    };
                };
            };
        };
    return sumClosest;
};

int main() {
    vector<int> nums = {0,0,0};
    cout<<threeSumClosest(nums,1)<<endl;

    return 0;
}; */

/* better solution of O(N^2) ==> using twi pointers */
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int result = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.size() - 2; i++) {
            int left = i + 1, right = nums.size() - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];

                if (abs(target - sum) < abs(target - result))
                    result = sum;

                if (sum == target) return target;
                else if (sum < target) left++;
                else right--;
            }
        }

        return result;
    }
};