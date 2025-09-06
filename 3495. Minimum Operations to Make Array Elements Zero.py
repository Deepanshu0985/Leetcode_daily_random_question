from typing import List
def findsteps(l,r):
    steps = 0 
    S= 1
    L=1
    
    while L<=r:
        R = (L*4) -1
        start = max(l,L)
        end = min(r,R)
        
        if start<=end:
            steps+=(end-start+1)*S
        L= L*4
        S+=1
    return steps
        
def minOperations( queries: List[List[int]]) -> int:
    steps = 0 
    for query in queries:
        l = query[0]
        r = query[1]
        steps+=findsteps(l,r)//2
    
    return steps

queries = [[1,2],[2,4]]
print(minOperations(queries))