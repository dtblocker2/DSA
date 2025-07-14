class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        output = 0
        #how to write below operation of traversing list on in one direction
        for i in range(len(nums)):
            for j in range(1,len(nums)-i):
                if (nums[i]*nums[i+j])% k == 0:
                    output+= 1
        
        return output

''' Shit solution with time complexity O(n^2)'''