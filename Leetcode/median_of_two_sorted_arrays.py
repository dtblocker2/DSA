class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Make sure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        x = len(nums1)
        y = len(nums2)
        
        start = 0
        end = x

        while start <= end:
            partitionX = (start + end) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            # If partitionX is 0, use -inf for maxLeftX
            # If partitionX is length of input, use +inf for minRightX
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Found the right partition
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            
            elif maxLeftX > minRightY:
                # Move left in nums1
                end = partitionX - 1
            else:
                # Move right in nums1
                start = partitionX + 1

'''
Let's break down how this solution works:

First, we ensure nums1 is the shorter array to optimize the binary search.

The algorithm uses binary search to find the correct partition point in both arrays where:

Elements to the left of partition in nums1 are smaller than elements to the right of partition in nums2
Elements to the left of partition in nums2 are smaller than elements to the right of partition in nums1
For each partition:

We calculate partitionX in nums1
We calculate corresponding partitionY in nums2
We find the elements around these partition points
We check if this is the correct partition
When we find the correct partition:

If total length is even, median is average of max of left elements and min of right elements
If total length is odd, median is max of left elements

'''