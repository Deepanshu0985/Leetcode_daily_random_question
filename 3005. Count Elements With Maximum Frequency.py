from collections import Counter
from typing import List
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res =0
        max_freq = max([i for i in freq.values()])
        for i in freq.values():
            if i == max_freq:
                res+=i
        return res

        