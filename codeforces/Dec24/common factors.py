class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        x=0
        listA = []
        listB = []
        for i in range(1,a+1):
            if a%i==0:
                listA.append(i)
        for i in range(1,b+1):
            if b%i==0:
                listB.append(i)
        
        for i in listB:
            for j in listA:
                if i ==j:
                    x+=1
        
        return x

print(Solution().commonFactors(2020,2025))