class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n==1:
            return 0
        m = 0
        k=n//2
        while k>0:
            g=n
            if n%2 != 0:
                n = (n+1)
                g=n-1
            k = g//2
            n /= 2
            m += k
            print(n,k)
        return int(m)

A = Solution()

while True:
    t = int(input('t: '))
    print(A.numberOfMatches(t))


# or simple solution is 
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1