class Solution:
    def numWaterBottles(self, b: int, e: int) -> int:
        res = b
        while b//e:
            rem =b%e
            res+=b//e
            b = rem+(b//e)
        return res
        