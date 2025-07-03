class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        coord_t = 0
        g_list = []
        for x in target:
            coord_t += abs(x)

        for x in ghosts:
            coord_g = 0
            for i in range(0,2):
                coord_g += abs(x[i]-target[i])
            g_list.append(coord_g)
        # print(g_list)

        for x in g_list:
            if coord_t >= x:
                # print(f"t:{coord_t}\nx:{x}")
                return False
        return True

print(Solution().escapeGhosts(ghosts = [[2,0]], target = [1,0]))