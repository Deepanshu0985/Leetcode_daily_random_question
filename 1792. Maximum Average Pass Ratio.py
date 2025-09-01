import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p,s):
            curravg = p/s
            newavg = (p+1)/(s+1)
            
            return newavg - curravg
        
        heap = [(-gain(p,s),p,s) for p,s in classes] 
        heapq.heapify(heap)
        
        while extraStudents:
            g,p,s = heapq.heappop(heap)
            p+=1
            s+=1
            heapq.push(heap,(-gain(p,s),p,s))
            extraStudents-=1
        
        return sum(p/s for _ in heap)/len(classes)
        