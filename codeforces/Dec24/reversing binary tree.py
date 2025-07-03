class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        n=1
        while (2**(2*n)) < len(root)+2:
            temp_list = []
            for index in range((2**(2*n-1)-1),(2**(2*n)-1)):
                temp_list.append(root[index])
            temp_list.reverse()
            i = 0
            for index in range((2**(2*n-1)-1),(2**(2*n)-1)):
                root[index] = temp_list[i]
                i += 1

            n += 1
        return root


print(Solution().reverseOddLevels([0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]))