class Solution(object):
    def minOperations(self, nums1: list[int], nums2: list[int]):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)

        def swap(i):
            nums1[i], nums2[i] = nums2[i], nums1[i]
        
        nums1_d = nums1[:]
        nums2_d = nums2[:]

        def max_ele(lst):
            max_element = lst[0]
            for i in range(n):
                if lst[i] > max_element:
                    max_element = lst[i]
            return max_element
        
        x = max_ele(nums1_d)
        y = max_ele(nums2_d)

        if 