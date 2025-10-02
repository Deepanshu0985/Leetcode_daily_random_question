class Solution:
    def maxBottlesDrunk(self, b: int, e: int) -> int:
        res = b
        while b-e >= 0:
            b = b-e
            res+=1
            e+=1
            b+=1
        return res

        
        