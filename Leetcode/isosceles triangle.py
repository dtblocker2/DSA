class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        different_sides = set(nums)
        k = len(different_sides)

        M=max(nums)
        if sum(nums) <= 2*M:
            return "none"

        match k:
            case 3:
                return "scalene"
            case 2:
                return "isosceles"
            case 1:
                return "equilateral"