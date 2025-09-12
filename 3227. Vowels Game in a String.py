class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return len([ch for ch in s if ch in "AEIOUaeiou"])/2!=0

        

        