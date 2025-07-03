class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        lst = nums[:]
        t = len(lst)
        for _ in range(len(lst)-k):
            max_num = lst[0]
            k=0
            for i in range(t):
                # try:
                #     l = lst[i]
                # except IndexError:
                #     continue
                l=lst[i]
                if l < max_num:
                    max_num=lst[i]
                    k=i
            print(lst)
            lst.pop(k)
            t-=1
        return lst
    
A = Solution()
print(A.maxSubsequence([-1,-2,3,4],3))