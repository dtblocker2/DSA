class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = nums.copy()
        for i in range(len(nums)-1):
            if nums[-2-i] < nums[-1-i]:
                for j in range(len(nums)-1-i):
                    if nums[j] > nums[i]:
                        nums[j],nums[i] = nums[i],nums[j]
                
                for k in range(len(nums)-1-i):
                    for m in range(len(nums)-1-i-k):
                        if nums[m] < nums[k]:
                            nums[m],nums[k] = nums[k], nums[m]
                break

        if k != nums:
            return None
        nums.sort()