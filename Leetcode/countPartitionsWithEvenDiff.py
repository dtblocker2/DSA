class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        y=0
        sumOfArr = 0
        sum2=0

        for i in nums:
            sumOfArr += i

        for i in range(len(nums)-1):
            sumOfArr -= nums[i]
            sum2 += nums[i]
            if (abs(sumOfArr-sum2))%2 == 0:
                y+=1
        return y