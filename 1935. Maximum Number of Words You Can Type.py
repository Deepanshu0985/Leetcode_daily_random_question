from collections import Counter
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        brok = Counter(brokenLetters)
        n = len(words)
        
        for word in words:
            for b in brokenLetters:
                if b in word:
                    n-=1
                    break


        return n

        