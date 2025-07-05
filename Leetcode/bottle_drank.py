class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty_bottles = numBottles
        bottle_drank = numBottles
        new_bottles = empty_bottles // numExchange

        while new_bottles>0:
            empty_bottles = empty_bottles % numExchange
            bottle_drank += new_bottles
            
            empty_bottles += new_bottles
            new_bottles = empty_bottles // numExchange
        return bottle_drank

A = Solution()

print(A.numWaterBottles(9,3))
