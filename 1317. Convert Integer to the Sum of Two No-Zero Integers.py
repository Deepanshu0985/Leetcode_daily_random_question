from typing import List
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        t = 0
        for i in range(1,n+1):
            t = i
            if (t%10 != 0 and '0' not in str(t))and  ((n-t) %10 != 0 and '0' not in str(n-t)) :
                break
        return [t,n-t]

        
        